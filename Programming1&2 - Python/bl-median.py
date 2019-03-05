a=[]
line=raw_input()
while line!="end":
	a.append(int(line))
	line=raw_input()


i=0
while i<len(a)-1:
   p=i
   j=i+1
   while j<len(a):
      if a[j] < a[p]:
         p=j
      j+=1
    
   tmp= a[p]
   a[p]=a[i]
   a[i]=tmp
   
   i+=1 

if len(a)%2==0:
	m=(len(a)+1)/2
	print a[m]
else:
	m=len(a)/2
	print a[m]
