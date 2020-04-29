line=raw_input()

while line != "end":
   i=0 
   while i<len(line) and line[len(line)-i-1] == " " :
       i=i+1  
   print line[:len(line)-i]
   line= raw_input()

