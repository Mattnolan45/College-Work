import sys

a=sys.stdin.readline()
while a:
   a=a.strip()
   total=0
   d=0
   u=0
   l=0 
   p=0
   for c in a:
       if c.isdigit():
          d=1
       elif c.isupper():
          u=1
       elif c.islower():
          l=1
       else:
          p=1
       total=u+d+l+p
   print(total)
   a=sys.stdin.readline()

