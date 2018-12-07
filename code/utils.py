import math
import config
from pylab import *
import matplotlib.pyplot as plt
import math

def load_txt(filename):
    v = []
    file = open(filename, 'r')
    for i in file.readlines():
        i = i.split(' ')  # 文件以“ ”分隔
        v.append(eval(i[0]))
    return v

def show_convergence_rate():
    v = config.get_value("CONVERGENCE_RATE_LIST")
    x = []
    for i in range(len(v)):
        x.append(i+1)
    plot(v)
    show()


def znormalize(x):
    M2 = float(0.0)
    mean = float(0.0)
    for i in range(len(x)):
        delta = x[i] - mean
        mean += delta/float(i+1)
        M2 += delta*(x[i]-mean)
    std = math.sqrt(M2 / (float(int(len(x)) - 1)))
    for i in range(len(x)):
        x[i] -= mean
    if std <= 0:
        return x
    for i in range(len(x)):
        x[i] /= std
    return x

def Replace_Elite(population):
    el = config.get_value("Elite_list")
    if (len(el) == 0):
        el = population
        config.set_value("Elite_list", el)
    else:
        for i in population:
            mmin = min(el)
            idx = el.index(min(el))
            if (i > mmin):
                el[idx] = i
        config.set_value("Elite_list", el)
    return el

def show_swarm_distribution():
    Xi = config.get_value("Xi")
    Xj = config.get_value("Xj")
    #Wi = config.get_value("Wi")
    #Wj = config.get_value("Wj")
    plt.scatter(Xi, Xj)
    plt.show()
    #plt.scatter(Wi, Wj)
    #plt.show()

def update_chaos_seed_logistic():
    CHAOS_SEED = config.get_value("CHAOS_SEED")
    for i in range(len(CHAOS_SEED)):
        CHAOS_SEED[i] = CHAOS_SEED[i]*4.0*(1-CHAOS_SEED[i])
    config.set_value("CHAOS_SEED", CHAOS_SEED)
def update_chaos_seed_cube():
    CHAOS_SEED = config.get_value("CHAOS_SEED")
    for i in range(len(CHAOS_SEED)):
        CHAOS_SEED[i] = 4.0*math.pow(CHAOS_SEED[i], 3) - 3.0*CHAOS_SEED[i]
    config.set_value("CHAOS_SEED", CHAOS_SEED)

def CHAOS_INIT():
    seeds = []
    for i in range(config.get_value("pop_size")):
        CHAOS_SEED = config.get_value("CHAOS_SEED")
        wmin = config.get_value("wmin")
        wmax = config.get_value("wmax")
        len = config.get_value("series_length")
        tw1 = int(wmin + CHAOS_SEED[1]*(wmax-wmin))
        tw2 = int(wmin + CHAOS_SEED[3]*(wmax-wmin))
        twi = int((len - tw1)*CHAOS_SEED[0])
        twj = int((len - tw2)*CHAOS_SEED[2])
        seeds.append([twi, tw1, twj, tw2])
        if config.get_value("CHAOS_ALGO") == "logistic":
            update_chaos_seed_logistic()
        if config.get_value("CHAOS_ALGO") == "cube":
            update_chaos_seed_cube()

    return seeds

