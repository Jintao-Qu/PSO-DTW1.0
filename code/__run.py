from main import *
import globalvar as gl

from numpy import *
import matplotlib
from pylab import *
import subprocess
filename = "pic/pic_carcount.txt"
gl._init()
f = open(filename, "w")
gl.set_value("f", f)
gl.set_value("CRAZY_PSO", 0.002)#2e-3
gl.set_value("Elite", True)
gl.set_value("Elite_list", [])

for i in range(10):
   gl.set_value("Elite_list", [])
   f = open(filename, "w")
   gl.set_value("f", f)
   main(filename="data/carcount.txt", wmin=5, wmax=7, display=True)
   f.close()
   v=[]
   rf=open(filename, 'r')
   for j in rf.readlines():
      v.append(eval(j))
   plot(v)
   show()


