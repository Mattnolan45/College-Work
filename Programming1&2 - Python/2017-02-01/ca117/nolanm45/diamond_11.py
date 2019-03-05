import sys
n=int(sys.argv[1])

h=n*2
i=1
while i<h:
   print(" "*abs(n-i),end="")
   if i<=n:
      print("* " * (i-1) + "*")
   elif n<i:
      print("* " * (h-i-1) +"*")
   i+=1
