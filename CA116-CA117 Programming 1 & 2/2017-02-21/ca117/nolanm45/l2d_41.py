import sys



def l2d(f):
    f=f.readlines()
    a=[]
    d={}
    for line in f:
        a.append(line.strip().split())
    i=0
    while i<len(a[0]):
       d[a[0][i]]=a[1][i]
       i+=1
    return(d)
