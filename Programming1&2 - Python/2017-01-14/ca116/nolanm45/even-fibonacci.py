import sys
n=int(sys.argv[1])


total=0
j=0
k=1
i=0
while i<n:
  if k<n:
    tmp=k
    k=j+k
    j=tmp
    if k%2==0:
		total=total+k
  i+=1
	
print total





