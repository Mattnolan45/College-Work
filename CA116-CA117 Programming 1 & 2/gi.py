import sys
s=sys.argv[1]

palindrome=""
i=0
while i<len(s) :
	palindrome=palindrome+s[len(s)-1-i]
	i+=1

	


if s==palindrome:
	print "yes"
else:
	print "no"

