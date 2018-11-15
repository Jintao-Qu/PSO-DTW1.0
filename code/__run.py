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

for i in range(10):
   f = open(filename, "w")
   gl.set_value("f", f)
   main(filename="data/carcount.txt", wmin=5, wmax=7, display=True)
   f.close()
   v=[]
   rf=open(filename,'r')
   for j in rf.readlines():
      v.append(j)
   plot(v)
   show()


