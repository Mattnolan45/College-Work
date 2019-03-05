import sys
s= sys.argv[1]

total =1
i=0
while i<len(s):
   total =total*int(s[i])
   print total
   i=i+1

