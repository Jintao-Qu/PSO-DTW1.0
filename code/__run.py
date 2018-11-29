from main import *
import config
import utils
import visited

for i in range(10):
    config._init()
    visited._init_visited_set()
    filename = config.get_value("filename")

    main(filename=filename, wmin=config.get_value("wmin"), wmax=config.get_value("wmax"),
         pop_size=config.get_value("pop_size"), max_evaluations=config.get_value("max_evaluations"), display=True)

    if(config.get_value("SHOW_CONVERGENCE_RATE")):
        utils.show_convergence_rate()
    if(config.get_value("SHOW_SWARM_DISTRIBUTION")):
        utils.show_swarm_distribution()




