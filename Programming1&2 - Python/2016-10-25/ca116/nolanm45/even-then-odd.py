a=[]
b=[]
line=raw_input()

while line!= "end":
	if int(line)%2==0:
		a.append(int(line))
	else :
		b.append(int(line))
	line=raw_input()

i=0
while i<len(a):
	print a[i]
	i+=1
i=0
while i<len(b):
	print b[i]
	i+=1