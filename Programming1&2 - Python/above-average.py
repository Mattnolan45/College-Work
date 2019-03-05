line=raw_input()
a=[]


while line!= "end":
   a.append(int(line))
   line=raw_input()

if len(a)!=0:
   average=0
   total=0
   i=0
   while i<len(a):
       total=total+a[i]
       i+=1
       average=total/len(a)


j=0
while j<len(a):
   if a[j]>average:
      print a[j]
   j+=1
      
    
    
