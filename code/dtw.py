from numpy import array, zeros, argmin, inf, ndim
from scipy.spatial.distance import cdist
from numpy.linalg import norm

def argmin(x):
    mn = x[0]
    mni=0
    for i in range(len(x)):
        if(x[i]<mn):
            mn=x[i]
            mni=i
    return mni

def compute(x ,y ,window_size):
    r, c = len(x), len(y)
    slope = ((float(c))/(float(r)))
    cost = zeros((len(x)+1,len(y)+1))
    D = zeros((len(x) + 1, len(y) + 1))
    weights = zeros((len(x) + 1, len(y) + 1))
    cost[0,0]=(x[0]-y[0])*(x[0]-y[0])
    cost[0,1]=(x[0]-y[1])*(x[0]-y[1])
    cost[1,0]=(x[1]-y[0])*(x[1]-y[0])
    cost[1,1]=(x[1]-y[1])*(x[1]-y[1])
    i = 2
    offset = 4
    while i<len(x):
        jj=int(round(i*slope))
        j_start=max(2,jj-window_size)
        j_end=min(int(len(y)),jj+window_size+1)
        j = max(2,j_start-offset)
        while j<j_start:
          cost[i][j]=inf
          j +=1
        j = j_start
        while j < j_end:
            cost[i][j] = x[i] - y[j]
            cost[i][j] *= cost[i][j]
            j += 1
        j = j_end
        while j < min(int(len(y)),j_end+offset+1):
            cost[i,j] = inf
            j += 1
        i +=1


    D[0][0]=2*cost[0][0]
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
