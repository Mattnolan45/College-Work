import sys
n=sys.stdin.read().split()

i=0
while i<len(n):
	if n[i].isdigit():
		print n[i]
	i+=1