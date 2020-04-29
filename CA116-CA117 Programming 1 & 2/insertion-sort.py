a=[]
line=raw_input()

while line!="end":
   a.append(int(line))
   line=raw_input()

n=input()
m=n
a.append(n)
i=1
while i< len(a):
    v=a[i]
    p=i 
    while 0<p and a[p-1]>v:
       a[p]=a[p-1]
       p=p-1
       a[p]=v
    
    i+=1
k=0
j=0        
while j<len(a) and a[k]!=m:
  k=len(a)-1-j 
  j+=1

print k

