import sys



def main():
    lines=sys.stdin.readlines()
    d={}
    total=0
    for name in lines:
        name=name.strip()
        d[name]= len(name)
        total+=len(name)
    average=total/len(d)
    print(d.items())
    d2={v:k for k,v in d.items()}
    print("Average: {:.2f}".format(average))
    print(d2)
    for n in d2.keys():
        if int(n)>average:
           print(d2[n])
        



if __name__=="__main__":
   main()
