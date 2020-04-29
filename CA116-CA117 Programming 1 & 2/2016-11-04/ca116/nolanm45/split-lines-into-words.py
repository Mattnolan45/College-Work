a=[]

s=raw_input()
while s!= "end":
	while s!=" ":
		a.append(s)
		s=raw_input()

i=0
while i<len(a):
	print a[i]
	i+=1