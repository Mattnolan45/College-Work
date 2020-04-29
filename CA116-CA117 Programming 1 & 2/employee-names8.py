a=[]
b=[]
line=raw_input()

i=0
while line!="end":
    a.append(line[:8])
    b.append(line[9:])
    line=raw_input()

j=0
k=0
line=raw_input()
while line!="end":
      i=0
      while i<len(a):
         if a[i]==line:
            print b[i]
         i+=1
      line=raw_input()
