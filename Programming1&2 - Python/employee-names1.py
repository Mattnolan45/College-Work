import sys
a={}

with open ("employees.txt","r") as f:
	b=f.readlines()
	i=0
	while i<len(b):
		a[i]=b[i].split(" ")
		a[b[i][0]]=b[i][2].strip()
		i+=1

lines=sys.stdin.readlines()
j=0
while j<len(lines):
	print b[lines[j].strip()]
	j+=1
