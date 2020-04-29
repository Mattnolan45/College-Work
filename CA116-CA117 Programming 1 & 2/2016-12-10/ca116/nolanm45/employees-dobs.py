import sys
a={}
c={}

import sys
a={}
c={} 

with open ("employees.txt","r") as f:
	b=f.readlines()
	i=0
	while i<len(b):
		b[i]=b[i].split()
		a[b[i][0]]=c
                c[b[i][0]]=b[i][1]
                i+=1



               
lines=sys.stdin.readlines()
j=0
while j<len(lines):
     print " ".join(c[lines[j].strip()])
     j+=1