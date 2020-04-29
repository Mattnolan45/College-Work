import sys
n=sys.argv[1]
a=[]


j=0
k=1
i=0
while i <int(n) :
  if k<int(n):
    a.append(k)
    tmp=k
    k=j+k
    j=tmp
  i = i+1
  
i=0
total=0
while i<len(a):
	if a[i]%2==0:
		total=total+int(a[i])
	i+=1



print total