a=[]
b=[]
line=raw_input()

while line!="end":
   a.append(line)
   line=raw_input()

line=raw_input()
while line!="end":
   b.append(int(line))
   line=raw_input()

i=0
while i<len(b):
   print a[b[i]]
   i+=1
