import sys
s=sys.argv[1]
t=int(sys.argv[2])


if t==10:
    print(s)
else:
   total=0
   i=0
   while i<len(s):
      total=total+int(s[(len(s)-1-i)]) * t**i
      i+=1
   print(total)

