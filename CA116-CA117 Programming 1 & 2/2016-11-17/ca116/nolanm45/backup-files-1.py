import os
files = os.listdir(".")         
pattern=".bak"


i = 0
while i < len(files):
  j=0
  while j<len(files[i]) and files[i][-4:]!= pattern:
     j+=1 
  if j<len(files):
     files[i]=files[i]+pattern
  
  print files[i]

  i+=1
