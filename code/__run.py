from main import *
import globalvar as gl
import utils

gl._init()
for i in range(10):
    filename = gl.get_value("filename")
    if(gl.get_value("SHOW_CONVERGENCE_RATE")):
        picfilename = gl.get_value("scr_picfilename")
        f = open(picfilename, "w")
        gl.set_value("f_show_convergence_rate", f)

    main(filename=filename, wmin=gl.get_value("wmin"), wmax=gl.get_value("wmax"),
         pop_size=gl.get_value("pop_size"), max_evaluations=gl.get_value("max_evaluations"), display=True)

    if(gl.get_value("SHOW_CONVERGENCE_RATE")):
        utils.show_convergence_rate()


