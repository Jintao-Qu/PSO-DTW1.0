import inspyred.swarm
import globalvar as gl
from inspyred.ec import Individual
import copy
import timeseriesproblem
from random import Random

class pso(inspyred.ec.EvolutionaryComputation):
    """Represents a basic particle swarm optimization algorithm.

    This class is built upon the ``EvolutionaryComputation`` class making
    use of an external archive and maintaining the population at the previous
    timestep, rather than a velocity. This approach was outlined in
    (Deb and Padhye, "Development of Efficient Particle Swarm Optimizers by
    Using Concepts from Evolutionary Algorithms", GECCO 2010, pp. 55--62).
    This class assumes that each candidate solution is a ``Sequence`` of
    real values.

    Public Attributes:

    - *topology* -- the neighborhood topology (default topologies.star_topology)

    Optional keyword arguments in ``evolve`` args parameter:

    - *inertia* -- the inertia constant to be used in the particle
      updating (default 0.5)
    - *cognitive_rate* -- the rate at which the particle's current
      position influences its movement (default 2.1)
    - *social_rate* -- the rate at which the particle's neighbors
      influence its movement (default 2.1)

    """

    def __init__(self, random):
        inspyred.ec.EvolutionaryComputation.__init__(self, random)
        self.topology = inspyred.swarm.topologies.star_topology
        self._previous_population = []
        self.selector = self._swarm_selector
        self.replacer = self._swarm_replacer
        self.variator = self._swarm_variator
        self.archiver = self._swarm_archiver

    def _swarm_archiver(self, random, population, archive, args):
        if len(archive) == 0:
            return population[:]
        else:
            new_archive = []
            for i, (p, a) in enumerate(zip(population[:], archive[:])):
                if p < a:
                    new_archive.append(a)
                else:
                    new_archive.append(p)
            return new_archive

    def _swarm_variator(self, random, candidates, args):
        inertia = args.setdefault('inertia', 0.5)
        cognitive_rate = args.setdefault('cognitive_rate', 2.1)
        social_rate = args.setdefault('social_rate', 2.1)
        if len(self.archive) == 0:
            self.archive = self.population[:]
        if len(self._previous_population) == 0:
            self._previous_population = self.population[:]
        neighbors = self.topology(self._random, self.archive, args)
        offspring = []
        for x, xprev, pbest, hood in zip(self.population,
                                         self._previous_population,
                                         self.archive,
                                         neighbors):
            nbest = max(hood)
            #nbest = gl.get_value("gbestx")
            particle = []

            for xi, xpi, pbi, nbi in zip(x.candidate, xprev.candidate,
                                         pbest.candidate, nbest.candidate):
                value = (xi + inertia * (xi - xpi) +
                         cognitive_rate * random.random() * (pbi - xi) +
                         social_rate * random.random() * (nbi - xi))
                if (random.random() < gl.get_value("CRAZY_PSO")):
                    t = random.random()
                    value += 1+t
                particle.append(int(value))
            particle = self.bounder(particle, args)
            offspring.append(particle)
        return offspring

    def _swarm_selector(self, random, population, args):

        t_updated = gl.get_value("t_updated")
        gl.set_value("t_updated", t_updated+1)
        if(gl.get_value("t_updated") - gl.get_value("t_lastupdate") >= gl.get_value("TCONV")):
            #print("@@@@@@@@@","re_init")
            #print(gl.get_value("t_updated"), gl.get_value("t_lastupdate"), gl.get_value("TCONV"))
            num_generated = gl.get_value("pop_size")
            i = 0
            initial_cs = []
            while i < num_generated:
                cs = self.generator(random=self._random, args=self._kwargs)
                initial_cs.append(cs)
                i += 1
            self.logger.debug('evaluating initial population')
            initial_fit = self.evaluator(candidates=initial_cs, args=self._kwargs)
            population = []
            for cs, fit in zip(initial_cs, initial_fit):
                if fit is not None:
                    ind = Individual(cs, self.maximize)
                    ind.fitness = fit
                    population.append(ind)
                else:
                    self.logger.warning('excluding candidate {0} because fitness received as None'.format(cs))
            self.logger.debug('population size is now {0}'.format(len(population)))
            self.archive = []
            #self.num_evaluations += len(initial_fit)
            #gl.set_value("t_lastupdate", gl.get_value("t_updated"))
            #return population
        if( max(population).fitness < gl.get_value("gbest") ):
            gl.set_value("gbest", max(population).fitness)
            gl.set_value("gbestx", max(population))
            gl.set_value("t_lastupdate", gl.get_value("t_updated"))
        f = gl.get_value("f")
        f.write(str(gl.get_value("gbest")))
        f.write('\n')
        return population
    '''
            if(gl.get_value("Elite") == False):
                f = gl.get_value("f")
                f.write(str(max(population).fitness))
                f.write('\n')
                return population
    '''
    '''
            el = gl.get_value("Elite_list")
            if(len(el)==0):
                el = population
                gl.set_value("Elite_list", el)
            else:
                g_best = max(el).fitness
                for i in population:
                    mmin = min(el)
                    idx = el.index(min(el))
                    if(i > mmin):
                        el[idx] = i
                    if(i.fitness < g_best):
                        gl.set_value("t_lastupdate", gl.get_value("t_updated"))
                gl.set_value("Elite_list", el)
            f = gl.get_value("f")
            f.write(str(max(el).fitness))
            f.write('\n')
    '''

    def _swarm_replacer(self, random, population, parents, offspring, args):
        self._previous_population = population[:]
        return offspring

