def _init():
    global _global_dict
    _global_dict = {}
    _global_dict["failename"] = "data/carcount.txt"
    _global_dict["CRAZY_PSO"] = 0.1  # 2e-3
    _global_dict["pop_size"] = 16
    _global_dict["max_evaluations"] = 4800
    _global_dict["IF_Elite"] = True
    _global_dict["Elite_list"] = []
    _global_dict["t_lastupdate"] = 0
    _global_dict["t_updated"] = 0
    _global_dict["TCONV"] = 100
    _global_dict["gbest"] = 0x3f3f3f3f
    _global_dict["Elite_list"] = []
    _global_dict["FORCE_NOT_OVERLAP"] = True
    _global_dict["DTW_ALGO"] = "Pierre_DTW" # CUSTOM_DTW, Pierre_DTW
    _global_dict["SHOW_CONVERGENCE_RATE"] = True
    _global_dict["scr_picfilename"] = "pic/pic_carcount.txt"
def set_value(name, value):
    _global_dict[name] = value

def get_value(name):
    return _global_dict[name]