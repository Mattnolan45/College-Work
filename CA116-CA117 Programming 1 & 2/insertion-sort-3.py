
a=[]
line=raw_input()

while line!="end":
   a.append(int(line))
   line=raw_input()

n=input()
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


j=0
while j<len(a):
  print a[j]
  j+=1