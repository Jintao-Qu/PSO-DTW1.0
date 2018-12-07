from time import time
from random import Random
import inspyred
import timeseriesproblem
from utils import load_txt, CHAOS_INIT
import pso
import config
import globalvar as gl
def main(filename, wmin, wmax, pop_size, max_evaluations, prng=None, display=False):
    if prng is None:
        prng = Random()
        prng.seed(time())

    v = load_txt(filename)
    config.set_value("series_length", len(v))
    print("lenth of series: ", len(v))
    problem = timeseriesproblem.timeseriesproblem(dimensions=4, v=v, wmin=wmin, wmax=wmax)

    ea = pso.pso(prng)
    ea.terminator = inspyred.ec.terminators.evaluation_termination
    ea.topology = inspyred.swarm.topologies.ring_topology

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
        #print('Best Solution: \n{0}'.format(str(best)))
        print('Best Solution: \n{0}'.format(config.get_value("gbestx")))

        if "gbest_sum" in gl._global_dict:
            gl.set_value("gbest_sum", gl.get_value("gbest_sum")+config.get_value("gbest"))
        else:
            gl.set_value("gbest_sum", config.get_value("gbest"))
        return ea

#if __name__ == '__main__':
#   main(filename="data/carcount.txt", wmin=5, wmax=7, display=True)




