from inspyred.benchmarks import *
import bounder
import dtw
import config
class timeseriesproblem(Benchmark):
    def __init__(self, v, dimensions, wmin, wmax):
        Benchmark.__init__(self, dimensions)
        self.v = v
        self.len = len(self.v)
        self.wmin = wmin
        self.wmax = wmax
        
        self.bounder = bounder.bounder(len=self.len,lower_bound=[0, self.wmin, 0, self.wmin],
                                  upper_bound=[self.len, self.wmax, self.len, self.wmax])
        self.maximize = False
        self.global_optimum = [0 for _ in range(self.dimensions)]

    def generator(self, random, args):
        tw1 = random.randint(self.wmin, self.wmax)
        tw2 = random.randint(self.wmin, self.wmax)
        twi = random.randint(0, self.len-tw1)
        twj = random.randint(0, self.len-tw2)
        return [twi, tw1, twj, tw2]

    def evaluator(self, candidates, args):

        fitness = []
        if config.get_value("DTW_ALGO") == "CUSTOM_DTW":
            fitness = dtw.Costom_Dtw(candidates=candidates, v=self.v, dimensions=self.dimensions)
        if config.get_value("DTW_ALGO") == "Pierre_DTW":
            fitness = dtw.Pierre_DTW(candidates=candidates, v=self.v)
        return fitness