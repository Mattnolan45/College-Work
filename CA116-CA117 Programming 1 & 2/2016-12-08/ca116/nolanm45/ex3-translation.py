import sys
a={}


with open("translation.txt","r") as f:
     b=f.readlines()
     i=0
     while i<len(b):  
         b[i]=b[i].split()
         a[b[i][0]]=b[i][1].strip()
         i+=1


lines=sys.stdin.readlines()
j=0
while j<len(lines):
   c=lines[j].split()
   k=0
   while k<len(c):
        if c[k] in a:
           c[k]=a[c[k]]
        k+=1
   print " ".join(c)
   j+=1



