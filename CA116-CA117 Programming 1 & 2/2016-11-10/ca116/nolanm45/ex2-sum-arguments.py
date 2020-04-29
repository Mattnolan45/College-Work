import sys
s= sys.argv[1:]



if s!=0:

  total=0
  i=0
  while i<len(s):
     total=total+int(s[i])
     i+=1

 
print total
