
a=[]
b=[]

line1= raw_input()
while line1!= "end":
   a.append(int(line1))
   line1=raw_input()

line2=raw_input()
while line2!= "end":
   b.append(int(line2))
   line2=raw_input()

i=0
j=0
while i<len(a) and j<len(b):
     if a[i] < b[j]:
         print a[i]
         i+=1
     else :
         print b[j]
         j+=1


while i<len(a):
       print a[i]
       i+=1
while j<len(b):
       print b[j]
       j+=1
