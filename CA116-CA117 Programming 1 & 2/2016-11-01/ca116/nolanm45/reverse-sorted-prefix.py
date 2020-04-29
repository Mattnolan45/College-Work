a=[]

line=raw_input()
while line !="end":
	a.append(int(line))
	line=raw_input()

i=0
while i<len(a) and a[i+1]>=a[i]:
	i+=1

while len(a)!=0 and i>=0:
	print a[i]
	i-=1