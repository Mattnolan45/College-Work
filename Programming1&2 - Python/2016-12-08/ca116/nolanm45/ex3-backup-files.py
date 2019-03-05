import os
files = os.listdir(".")
pattern=".bak"


i=0
while i<len(files):
     if files[i][-4:]!= pattern:
          with open(files[i],"r") as f:
               a=f.read()
          with open(files[i]+pattern,"w") as g:
               g.write(a)
     i+=1 
