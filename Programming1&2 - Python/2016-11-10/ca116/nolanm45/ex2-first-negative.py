a=[]

line=raw_input()
while line!="end":
   a.append(int(line))
   line=raw_input()
  
i=0
while i<len(a):
    if a[i]<0:
         print a[i]
         i=i+len(a)
    i+=1
