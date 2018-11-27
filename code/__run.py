from main import *
import globalvar as gl

from numpy import *
import matplotlib
from pylab import *
import subprocess

filename = "data/carcount.txt"
wmin=5
wmax=7
picfilename = "pic/pic_carcount.txt"
gl._init()
f = open(picfilename, "w")
gl.set_value("f", f)
gl.set_value("CRAZY_PSO", 0.11)#2e-3
gl.set_value("pop_size", 16)
gl.set_value("max_evaluations", 4800)
gl.set_value("t_lastupdate", 0)
gl.set_value("t_updated", 0)
gl.set_value("TCONV", 100)
gl.set_value("gbest", 100)
for i in range(10):
   filename = "data/carcount.txt"
   wmin = 5
   wmax = 7
   picfilename = "pic/pic_carcount.txt"
   gl._init()
   f = open(picfilename, "w")
   gl.set_value("f", f)
   gl.set_value("CRAZY_PSO", 0.11)  # 2e-3
   gl.set_value("pop_size", 16)
   gl.set_value("max_evaluations", 4800)
   gl.set_value("Elite", True)
   gl.set_value("Elite_list", [])
   gl.set_value("t_lastupdate", 0)
   gl.set_value("t_updated", 0)
   gl.set_value("TCONV", 100)
   gl.set_value("gbest", 100)
   gl.set_value("Elite_list", [])
   f = open(picfilename, "w")
   gl.set_value("f", f)
   main(filename=filename, wmin=wmin, wmax=wmax,
        pop_size=gl.get_value("pop_size"), max_evaluations=gl.get_value("max_evaluations"), display=True)
   print(gl.get_value("t_updated"))
   f.close()
   v = []
   rf = open(picfilename, 'r')
   for j in rf.readlines():
      v.append(eval(j))
   plot(v)
   show()


