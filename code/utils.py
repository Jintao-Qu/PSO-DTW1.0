def load_txt(filename):
    v=[]
    file=open(filename,'r')
    for i in file.readlines():
        #i = i.strip('\n')  # 除去换行
        i = i.split(' ')  # 文件以“ ”分隔
        #if "" in i:  # 解决每行结尾有空格的问题
            #i.remove("")
        v.append(eval(i[0]))
    return v



