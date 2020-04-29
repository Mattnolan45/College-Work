import sys
n= int(sys.argv[1])


i=2
while i<n:
  k=2
  while k<i and i%k !=0:
     k+=1
  if k== i:
     print i 
  i+=1

