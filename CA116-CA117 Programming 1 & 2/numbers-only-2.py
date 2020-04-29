import sys
n=sys.stdin.read().split()

i=0
while i<len(n):
	k=n[i].split()
	if k[0].isdigit() or k[1].isidgit():
		print k

	i+=1
