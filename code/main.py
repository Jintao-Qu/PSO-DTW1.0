from time import time
from random import Random
import inspyred
import timeseriesproblem
from utils import CHAOS_INIT, SHOW_MOTIF
import pso
import config
import globalvar as gl
def main(data, wmin, wmax, pop_size, max_evaluations, prng=None, display=False):
    if prng is None:
        prng = Random()
        prng.seed(time())

    v = data
    config.set_value("series_length", len(v))
    problem = timeseriesproblem.timeseriesproblem(dimensions=4, v=v, wmin=wmin, wmax=wmax, random=prng)

    ea = pso.pso(prng)
    ea.terminator = inspyred.ec.terminators.evaluation_termination
    ea.topology = inspyred.swarm.topologies.ring_topology
    ea.observer = inspyred.ec.observers.default_observer

    seeds = []
    if config.get_value("CHAOS_ALGO") != "None":
        seeds = CHAOS_INIT()

    final_pop = ea.evolve(generator=problem.generator,
                          evaluator=problem.evaluator,
                          pop_size=pop_size,
                          seeds=seeds,
                          bounder=problem.bounder,
                          maximize=problem.maximize,
                          max_evaluations=max_evaluations,
                          neighborhood_size=5)

    if display:
        best = max(final_pop)
        print('Best Solution: \n{0}'.format(str(best)))
        #print('Best Solution: \n{0}'.format(config.get_value("gbestx")))
        if config.get_value("SHOW_MOTIF") == True:
            SHOW_MOTIF(data, best.candidate)
        if gl.get_value("gbest_sum") != "not found":
            gl.set_value("gbest_sum", gl.get_value("gbest_sum")+config.get_value("gbest"))
        else:
            gl.set_value("gbest_sum", config.get_value("gbest"))
        return ea

#if __name__ == '__main__':
#   main(filename="data/carcount.txt", wmin=5, wmax=7, display=True)




