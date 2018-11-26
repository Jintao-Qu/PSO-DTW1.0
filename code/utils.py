import math
def load_txt(filename):
    v=[]
    file=open(filename,'r')
    for i in file.readlines():
        #i = i.strip('\n')  # 除去换行
        i = i.split(' ')  # 文件以“ ”分隔
        #if "" in i:  # 解决每行结尾有空格的问题
            #i.remove("")
        v.append(eval(i[0]))
        #print("\rserieslength", len(v), end="")
    return v

def znormalize(x):
    M2 = float(0.0)
    mean = float(0.0)
    for i in range(len(x)):
        delta = x[i] - mean
        mean += delta/float(i+1)
        M2 += delta*(x[i]-mean)
    #print(M2,x, (float(int(len(x)) - 1)))
    std = math.sqrt(M2 / (float(int(len(x)) - 1)))
    for i in range(len(x)):
        x[i] -= mean
    if std <= 0:
        return x
    for i in range(len(x)):
        x[i] /= std
    return x
