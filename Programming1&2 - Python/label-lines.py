a = []
line =raw_input()


while line!="end" :
   a.append(line)
   line=raw_input()
   

n=len(a)
i=0

while i<n:
   print i,n,a[i] 
   i+=1
