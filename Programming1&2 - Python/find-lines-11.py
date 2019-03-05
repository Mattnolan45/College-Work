import sys
pattern= sys.argv[1]

line=raw_input()

while line !="end":
  i=0
  while i< len(line): 
    if line [i:i+len(pattern)]==pattern :
      print "yes"
    else :
      print "no"
    i=i+1
  line=raw_input()
     
