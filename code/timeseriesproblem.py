from inspyred.benchmarks import *
import bounder

class timeseriesproblem(Benchmark):
    def __init__(self,v,dimensions,wmin,wmax,dist):
        Benchmark.__init__(self,dimensions)
        self.dist=dist
        self.v=v
        self.len=len(self.v)
        self.wmin=wmin
        self.wmax=wmax
        
        self.bounder=bounder.bounder(len=self.len,lower_bound=[0, self.wmin, 0, self.wmin],
                                  upper_bound=[self.len, self.wmax, self.len, self.wmax])
        self.maximize = False
        self.global_optimum = [0 for _ in range(self.dimensions)]

    def generator(self,random,args):
        tw1=random.randint(self.wmin,self.wmax)
        tw2=random.randint(self.wmin,self.wmax)
        twi=random.randint(0,self.len-tw1)
        twj=random.randint(0,self.len-tw2)
        #print("###",[twi,tw1,twj,tw2])
        return [twi,tw1,twj,tw2]

    def evaluator(self, candidates, args):
        from numpy import array, zeros, argmin, inf, ndim
        from scipy.spatial.distance import cdist
        from numpy.linalg import norm
        fitness = []
        #dist = lambda x, y: norm(x - y, ord=1)
        for cc in candidates:
            #print("cc",cc)
            x=self.v[int(cc[0]):int(cc[0]+cc[1]+1)]
            x=array(x).reshape(-1,1)
            y=self.v[int(cc[2]):int(cc[2]+cc[3]+1)]
            y=array(y).reshape(-1,1)
            r, c = len(x), len(y)
            #if r==0 or c==0:
            #    print("##!!!")
            #    print(cc)

            D0 = zeros((r + 1, c + 1))
            D0[0, 1:] = inf
            D0[1:, 0] = inf
            D1 = D0[1:, 1:]
            for i in range(r):
                for j in range(c):
                    D1[i, j] = self.dist(x[i], y[j])

            C = D1.copy()  # deep copy
            warp=1
            for i in range(r):
                for j in range(c):
                    min_list = [D0[i, j]]
                    for k in range(1, warp + 1):
                        i_k = min(i + k, r - 1)  # the biggest index = r-1.
                        j_k = min(j + k, c - 1)
                        min_list += [D0[i_k, j], D0[i, j_k]]  # 3 data item in min_list
                    D1[i, j] += min(min_list)  # D1[i,j]+=the minimum data item
            if(cc[0]+cc[1]>=cc[2]) :
                fitness.append(inf)
            else:
                fitness.append(D1[-1, -1] / sum(D1.shape))
        return fitness
