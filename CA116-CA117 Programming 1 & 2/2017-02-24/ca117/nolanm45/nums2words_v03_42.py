import sys
d={}


i=0
with open(sys.argv[1],"r") as f:
         for line in f:
             line=line.split()
             d[str(i)]=line[0],line[1]  
             i+=1

for n in sys.stdin.readlines():
    print(" ".join([d[word][1] for word in n.split()]))
