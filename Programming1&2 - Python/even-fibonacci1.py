import sys
n=sys.argv[1]
a=[]

total=0
j=0
k=1
i=0
while i <int(n) :
  if k<int(n):
    a.append(k)
    tmp=k
    k=j+k
    j=tmp
    if a[i]%2==0:
		total=total+int(a[i])
  i+=1
	
print total





