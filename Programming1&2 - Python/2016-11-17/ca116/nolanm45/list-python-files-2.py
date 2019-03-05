import os
files = os.listdir(".")         

i = 0
while i < len(files):
  with open(files[i]) as f:
     a=f.read() 
  if files[i][-3] == "." and len(a)!=0:       
      print files[i]
  i = i + 1
