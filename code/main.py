from time import time
from random import Random
import inspyred
from numpy.linalg import norm
import timeseriesproblem
from utils import load_txt
import pso
import globalvar as gl
def main(filename, wmin, wmax, prng=None, display=False):
    if prng is None:
        prng = Random()
        prng.seed(time())

    v = load_txt(filename)
    print("len_v: ", len(v))

    problem = timeseriesproblem.timeseriesproblem(dimensions=4, v=v, wmin=wmin, wmax=wmax,
                                                  dist=lambda x, y: norm(x - y, ord=1))
    gl.set_value("problem", problem)
    ea = pso.pso(prng)
    ea.terminator = inspyred.ec.terminators.evaluation_termination
    ea.topology = inspyred.swarm.topologies.ring_topology
    final_pop = ea.evolve(generator=problem.generator,
                          evaluator=problem.evaluator,
                          pop_size=16,
                          bounder=problem.bounder,
                          maximize=problem.maximize,
                          max_evaluations=4800,
                          neighborhood_size=5)
    if display:
        if (gl.get_value("Elite") == False):
            best = max(final_pop)
        else:
            el = gl.get_value("Elite_list")
            best = max(el)
        print('Best Solution: \n{0}'.format(str(best)))
        return ea

#if __name__ == '__main__':
#   main(filename="data/carcount.txt", wmin=5, wmax=7, display=True)




