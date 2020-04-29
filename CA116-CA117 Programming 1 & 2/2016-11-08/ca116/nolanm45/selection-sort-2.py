line=raw_input()
a=[]

while line!="end":
    a.append(int(line))
    line=raw_input()

p=input()
i=p+1
while i<len(a):
   if a[i]<a[p]:
	p=i
   i+=1

print p

 

