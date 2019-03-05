import sys
pattern= sys.argv[1]



s=raw_input()
while s != "end":
   i=0 
   j=0
   while i<len(s): 
     if s[i:i+len(pattern)]== pattern:
        j=j+1
        i=i+len(pattern)
     else:
        i=i+1
   print j
   s=raw_input()


