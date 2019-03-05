import sys


with open(sys.argv[1]) as f:
    i=0
    total=0
    n=f.readlines()
    while i<len(n):
       total=total+int(n[i])
       i+=1
    print total


