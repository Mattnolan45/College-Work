a=[]
line=raw_input()

i=0
while line!="end":
   a.append(int(line))
   line=raw_input()

n=input()
while i<len(a) and a[i] <=n:
   i+=1

print i
