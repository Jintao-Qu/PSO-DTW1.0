import subprocess

pname = "C:\\Users\\JinTao\\Documents\\GitHub\\PSO-DTW1.0\\code\\cppcode.exe"
source = b"-s  \data\carcount.txt  -w  5  7  -k  5  -i  300  -v  yes"
p = subprocess.Popen(pname, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
result=p.communicate(input=source)
print(result)
