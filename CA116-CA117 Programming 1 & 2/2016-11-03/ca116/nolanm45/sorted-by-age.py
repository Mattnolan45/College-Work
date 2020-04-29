a=[]
b=[]
line=raw_input()

while line!="end":
    a.append(line[6:8])
    b.append(line[9:])
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
  

   tmp=b[p]
   b[p]=b[i]
   b[i]=tmp
   i+=1
   
 
j=0
while j<len(b):
   print b[j]
   j+=1
