import sys
c=[]

with open("words-1.txt","r") as f:
	a=f.readlines()

with open("words-2.txt","r") as g:
	b=g.readlines()

i=0
while i<len(b):
	if b[i] in a and  b[i] not in c:
		c.append(b[i])
	i+=1

for loops\