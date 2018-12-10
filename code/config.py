def _init():
    global _config_dict
    _config_dict = {}
    _config_dict["filename"] = "data/eog.txt"#dowjones, eog, carcount
    _config_dict["pop_size"] = 16
    _config_dict["max_evaluations"] = 4800
    _config_dict["wmin"] = 5
    _config_dict["wmax"] = 7
    _config_dict["gbest"] = 0x3f3f3f3f

    _config_dict["bounder"] = "attach"#attach, MOD, CRAZY
    _config_dict["CRAZY"] = 0.0
    _config_dict["IF_Elite"] = True
    _config_dict["Elite_list"] = []

    _config_dict["CRAZY_PSO"] = 0.0

    _config_dict["t_lastupdate"] = 0
    _config_dict["t_updated"] = 0
    _config_dict["TCONV"] = 0x3f3f3f3f

    _config_dict["FORCE_NOT_OVERLAP"] = True
    _config_dict["DTW_ALGO"] = "Pierre_DTW"# CUSTOM_DTW, Pierre_DTW

    _config_dict["SHOW_CONVERGENCE_RATE"] = True
    _config_dict["CONVERGENCE_RATE_LIST"] = []

    _config_dict["SHOW_SWARM_DISTRIBUTION"] = True
    _config_dict["SHOW_INIT_SWARM"] = True
    _config_dict["SHOW_SWARM_CYCLE"] = 100
    _config_dict["Xi"] = []
    _config_dict["Xj"] = []
    _config_dict["Wi"] = []
    _config_dict["Wj"] = []

    _config_dict["CHAOS_ALGO"] = "None" #logistic, cube, None
    _config_dict["CHAOS_SEED"] = [0.4, 0.4, 0.4, 0.4]

def set_value(name, value):
    _config_dict[name] = value

def get_value(name):
    return _config_dict[name]