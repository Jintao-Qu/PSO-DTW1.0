from time import time
from random import Random
import inspyred
from numpy.linalg import norm
import timeseriesproblem
from utils import load_txt
import pso

def main(filename, wmin, wmax, prng=None, display=False):
    if prng is None:
        prng = Random()
        prng.seed(time())

    v = load_txt(filename)

    problem = timeseriesproblem.timeseriesproblem(dimensions=4, v=v, wmin=wmin, wmax=wmax,
                                                  dist=lambda x, y: norm(x - y, ord=1))

    ea = pso.pso(prng)
    ea.terminator = inspyred.ec.terminators.evaluation_termination
    ea.topology = inspyred.swarm.topologies.ring_topology
    final_pop = ea.evolve(generator=problem.generator,
                          evaluator=problem.evaluator,
                          pop_size=100,
                          bounder=problem.bounder,
                          maximize=problem.maximize,
                          max_evaluations=300,
                          neighborhood_size=5)
    if display:
        best = max(final_pop)

        print('Best Solution: \n{0}'.format(str(best)))

        return ea

if __name__ == '__main__':
    main(filename="data/carcount.txt", wmin=5, wmax=7, display=True)




