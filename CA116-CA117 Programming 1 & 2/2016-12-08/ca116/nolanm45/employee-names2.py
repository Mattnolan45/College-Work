import sys
a={}
c={}


with open ("employees.txt","r") as f:
	b=f.readlines()
	i=0
	while i<len(b):
		b[i]=b[i].split(" ")
		c=b[i][0]
		a[b[i][0]]=c
		c["id"]=b[i][0]
		c["dob"]=b[i][1]
		c["name"]=b[i][2]
                i+=1

lines=sys.stdin.readlines()
j=0
while j<len(lines):
     print b[lines[j][c[name]].strip()]
     j+=1
       
   
