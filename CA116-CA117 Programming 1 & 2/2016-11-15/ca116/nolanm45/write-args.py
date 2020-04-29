import sys

s=sys.argv[1:]
with open(sys.argv[1],"w") as f:
     i=1
     while i<len(s):
         f.write(s[i]+"\n")
         i+=1
    
