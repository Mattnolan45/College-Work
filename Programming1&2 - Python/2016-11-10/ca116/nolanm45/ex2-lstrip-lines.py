
line=raw_input()
while line!= "end":
   i=0
   if line[0:]=="" or line[0]!=" ":
       print line[0:]
   while i<len(line) and line[i]==" ":
      i+=1
      if line[i]!=" ":
          print line[i:]
   line=raw_input() 
   
