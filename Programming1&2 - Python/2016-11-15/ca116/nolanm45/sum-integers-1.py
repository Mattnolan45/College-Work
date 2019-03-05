import sys
n=sys.stdin.readlines()

i=0
total=0
while i<len(n):
   total=total+int(n[i])
   i+=1

print total
