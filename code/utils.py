import math
import globalvar as gl
from pylab import *
def load_txt(filename):
    v = []
    file = open(filename, 'r')
    for i in file.readlines():
        i = i.split(' ')  # 文件以“ ”分隔
        v.append(eval(i[0]))
    return v

def show_convergence_rate():
    f = gl.get_value("f_show_convergence_rate")
    f.close()
    v = []
    picfilename = gl.get_value("scr_picfilename")
    rf = open(picfilename, 'r')
    for j in rf.readlines():
        v.append(eval(j))
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
