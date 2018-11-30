import inspyred.swarm
import config
from inspyred.ec import Individual
import utils
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
            particle = []

            for xi, xpi, pbi, nbi in zip(x.candidate, xprev.candidate,
                                         pbest.candidate, nbest.candidate):
                value = (xi + inertia * (xi - xpi) +
                         cognitive_rate * random.random() * (pbi - xi) +
                         social_rate * random.random() * (nbi - xi))
                if (random.random() < config.get_value("CRAZY_PSO")):
                    t = random.random()
                    value += 1+t
                particle.append(int(value))
            particle = self.bounder(particle, args)
            offspring.append(particle)
        return offspring

    def _swarm_selector(self, random, population, args):

        if(config.get_value("SHOW_SWARM_DISTRIBUTION")):
            for p in population:
                config.get_value("Xi").append(p.candidate[0])
                config.get_value("Wi").append(p.candidate[1])
                config.get_value("Xj").append(p.candidate[2])
                config.get_value("Wj").append(p.candidate[3])
        if(config.get_value("SHOW_SWARM_DISTRIBUTION")) and config.get_value("t_updated") == 0:
            utils.show_swarm_distribution()
        if (config.get_value("t_updated")+1) % config.get_value("SHOW_SWARM_CYCLE") == 0:
            utils.show_swarm_distribution()
        t_updated = config.get_value("t_updated")
        config.set_value("t_updated", t_updated+1)
        if(config.get_value("t_updated") - config.get_value("t_lastupdate") >= config.get_value("TCONV")):
            initial_cs = []
            if config.get_value("CHAOS_ALGO") != "None":
                initial_cs = utils.CHAOS_INIT()
            else:
                num_generated = config.get_value("pop_size")
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
        if( max(population).fitness < config.get_value("gbest") ):
            config.set_value("gbest", max(population).fitness)
            config.set_value("gbestx", max(population))
            config.set_value("t_lastupdate", config.get_value("t_updated"))
        if (config.get_value("SHOW_CONVERGENCE_RATE")):
            config.get_value("CONVERGENCE_RATE_LIST").append(config.get_value("gbest"))
        if (config.get_value("IF_Elite") == True):
            population = utils.Replace_Elite(population=population)
        return population


    def _swarm_replacer(self, random, population, parents, offspring, args):
        self._previous_population = population[:]
        return offspring

