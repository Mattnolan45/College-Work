line=raw_input()
output=""

while line!="end":
      i=0
      while i<len(line):
             if line[i]!= " ":
		     output += line[i]
             elif output!="":
                     print output
                     output=""
              elif == len(line)-1:
                      print output
                      output= ""
              i+=1
       line=raw_input()
