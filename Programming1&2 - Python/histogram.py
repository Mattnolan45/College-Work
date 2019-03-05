a=[]
line=raw_input()

while line!= "end":
	a.append(int(line))
	line=raw_input()

n=0
while n<10:
	i=0
	c=0
	while (i<len(a)):
		if (a[i] == n):
			c+=1
		i+=1
	print n, ("*" * c)
	n+=1