from numpy import array, zeros, argmin, inf, ndim
from scipy.spatial.distance import cdist
from numpy.linalg import norm
from numpy import array, zeros, argmin, inf, ndim
from scipy.spatial.distance import cdist
from numpy.linalg import norm
from math import log
import utils
import config
import visited
def argmin(x):
    mn = x[0]
    mni = 0
    for i in range(len(x)):
        if(x[i] < mn):
            mn = x[i]
            mni = i
    return mni

def compute(x ,y ,window_size):
    r, c = len(x), len(y)
    slope = ((float(c))/(float(r)))
    cost = zeros((len(x)+1, len(y)+1))
    D = zeros((len(x) + 1, len(y) + 1))
    weights = zeros((len(x) + 1, len(y) + 1))
    cost[0, 0] = (x[0]-y[0])*(x[0]-y[0])
    cost[0, 1] = (x[0]-y[1])*(x[0]-y[1])
    cost[1, 0] = (x[1]-y[0])*(x[1]-y[0])
    cost[1, 1] = (x[1]-y[1])*(x[1]-y[1])
    i = 2
    offset = 4
    while i < len(x):
        jj = int(round(i*slope))
        j_start = max(2, jj-window_size)
        j_end = min(int(len(y)), jj+window_size+1)
        j = max(2, j_start-offset)
        while j < j_start:
          cost[i][j] = inf
          j += 1
        j = j_start
        while j < j_end:
            cost[i][j] = x[i] - y[j]
            cost[i][j] *= cost[i][j]
            j += 1
        j = j_end
        while j < min(int(len(y)), j_end+offset+1):
            cost[i, j] = inf
            j += 1
        i += 1


    D[0][0] = 2*cost[0][0]
    weights[0][0]=float(2.0)
    D[0][1]=cost[0][1]+2*cost[0][0]
    weights[0][1]=float(3.0)
    D[1][0]=cost[1][0]+2*cost[0][0]
    weights[1][0]=float(3.0)
    D[1][1]=D[0][0]+2*cost[1][1]
    weights[1][1]=weights[0][0]+2

    i=2
    while i < len(x):
        jj=int(round(i*slope))
        j_start=max(2,jj-window_size)
        j_end=min(int(len(y)),jj+window_size+1)
        j = max(2,j_start-offset)
        while j < j_start:
            D[i][j] = inf
            j += 1

        j = j_start
        while(j < j_end):
            choice = []
            choice.append(D[i-1][j-2]+2*cost[i][j-1]+cost[i][j])
            choice.append(D[i-1][j-1]+2*cost[i][j])
            choice.append(D[i-2][j-1]+2*cost[i-1][j]+cost[i][j])
            k=argmin(choice)
            D[i][j]=choice[k]
            if k ==0 :
                weights[i][j]=weights[i-1][j-2]+3
            elif k == 1 :
                weights[i][j]=weights[i-1][j-1]+2
            elif k == 2 :
                weights[i][j]=weights[i-2][j-1]+3

            j += 1

        j = j_end
        while j < min(int(len(y)),j_end+offset+1):
            D[i][j]=inf
            j += 1

        i+=1


    return D[len(x)-1][len(y)-1]/weights[len(x)-1][len(y)-1]

def Pierre_DTW(candidates, v):
    fitness = []
    dist = lambda x, y: norm(x - y, ord=1)
    for cc in candidates:
        if (cc[0] + cc[1] >= cc[2]) and config.get_value("FORCE_NOT_OVERLAP"):
            fitness.append(inf)
        else:
            x = v[int(cc[0]):int(cc[0] + cc[1] + 1)]
            x = array(x).reshape(-1, 1)
            y = v[int(cc[2]):int(cc[2] + cc[3] + 1)]
            y = array(y).reshape(-1, 1)
            r, c = len(x), len(y)
            D0 = zeros((r + 1, c + 1))
            D0[0, 1:] = inf
            D0[1:, 0] = inf
            D1 = D0[1:, 1:]
            for i in range(r):
                for j in range(c):
                    D1[i, j] = dist(x[i], y[j])

            C = D1.copy()  # deep copy
            warp = 1
            for i in range(r):
                for j in range(c):
                    min_list = [D0[i, j]]
                    for k in range(1, warp + 1):
                        i_k = min(i + k, r - 1)  # the biggest index = r-1.
                        j_k = min(j + k, c - 1)
                        min_list += [D0[i_k, j], D0[i, j_k]]  # 3 data item in min_list
                    D1[i, j] += min(min_list)  # D1[i,j]+=the minimum data item

            fitness.append(D1[-1, -1] / sum(D1.shape))
    return fitness
def Costom_Dtw(candidates, v, dimensions):
    fitness = []
    for cc in candidates:

        if (cc[0] + cc[1] >= cc[2]) and config.get_value("FORCE_NOT_OVERLAP"):
            fitness.append(inf)
        else:
            key = str(cc[0])+"-"+str(cc[1])+"-"+str(cc[2])+"-"+str(cc[3])
            if key in visited._visited_dict:
                fitness.append(visited._visited_dict[key])
            else:
                x = v[int(cc[0]):int(cc[0] + cc[1])]
                y = v[int(cc[2]):int(cc[2] + cc[3])]
                x = utils.znormalize(x)
                y = utils.znormalize(y)
                dissim = compute(x, y, dimensions)
                dissim = dissim / log(float(max(len(x), len(y))))
                visited.set_value("key", dissim)
                fitness.append(dissim)
    return fitness