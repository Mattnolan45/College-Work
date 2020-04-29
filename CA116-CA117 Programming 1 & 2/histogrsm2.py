n=raw_input()
histogram = [0] * int(n)

line=raw_input()
while line!= "end":
   histogram[int(line)]+=1
   line=raw_input()

i=0
while i<n:
   print i,"*" * histogram[i]
   i+=1
