import sys
s=sys.argv[1]

total=0
n=0
i=0
while i<len(s):
	total=total+int(s[(len(s)-1-i)]) * 2**i
	i+=1
	
print total
