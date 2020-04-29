a=[]
b=[]
line=raw_input()

while line != "end":
	a.append(int(line))
	line=raw_input()

i=0
j=0
k=0
	
while j<999 and len(b)<=len(a) and k<len(a):
	if (a[k] == j):
		b.append(a[k])
		j+=1
	elif (a[k]!=j):
		k+=1
	k=0
	
	
	
	
	


n=0
while n<len(b):
	print b[n]
	n+=1
