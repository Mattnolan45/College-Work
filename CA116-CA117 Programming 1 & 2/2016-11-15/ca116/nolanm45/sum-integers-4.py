import sys

total=0
i=1
while i<len(sys.argv):

  with open(sys.argv[i],"r") as f:
      n=f.read().split()
      
      j=0
      while j<len(n):
         total=total+int(n[j])
         j+=1
  i+=1


print total

