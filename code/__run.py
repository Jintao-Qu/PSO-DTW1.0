from main import *
import globalvar as gl
import utils


for i in range(10):
    filename = "data/carcount.txt"
    wmin = 5
    wmax = 7
    gl._init()
    if(gl.get_value("SHOW_CONVERGENCE_RATE")):
        picfilename = gl.get_value("scr_picfilename")
        f = open(picfilename, "w")
        gl.set_value("f_show_convergence_rate", f)

    main(filename=filename, wmin=wmin, wmax=wmax,
         pop_size=gl.get_value("pop_size"), max_evaluations=gl.get_value("max_evaluations"), display=True)

    if(gl.get_value("SHOW_CONVERGENCE_RATE")):
      utils.show_convergence_rate()



