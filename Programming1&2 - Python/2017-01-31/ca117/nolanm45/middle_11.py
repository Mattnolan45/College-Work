import sys
s=sys.argv[1]


if len(s)%2==1:
   print(s[int(len(s)/2)])	
else:
   print("No middle character!")
