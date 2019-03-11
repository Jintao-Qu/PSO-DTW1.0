from main import *
import config
import utils
import visited
import globalvar as gl

gl._init_globalar()
config._init()
v = utils.load_txt(config.get_value("filename"))
for i in range(30):
    print("run...", i)
    config._init()
    visited._init_visited_set()
    filename = config.get_value("filename")

    main(data=v, wmin=config.get_value("wmin"), wmax=config.get_value("wmax"),
         pop_size=config.get_value("pop_size"), max_evaluations=config.get_value("max_evaluations"), display=True)

    if(config.get_value("SHOW_CONVERGENCE_RATE")):
        utils.show_convergence_rate()
    if(config.get_value("SHOW_SWARM_DISTRIBUTION")):
        utils.show_swarm_distribution()
print("Best_SUM= ", gl.get_value("gbest_sum"))



