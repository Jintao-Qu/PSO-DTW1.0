import math
import config
from pylab import *
import matplotlib.pyplot as plt
def load_txt(filename):
    v = []
    file = open(filename, 'r')
    for i in file.readlines():
        i = i.split(' ')  # 文件以“ ”分隔
        v.append(eval(i[0]))
    return v

def show_convergence_rate():

    v = config.get_value("CONVERGENCE_RATE_LIST")
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