import sys
import string

d={}
for line in sys.stdin:
	words=line.strip().split()
	for w in words:
		w=w.strip(string.punctuation).lower()
		if w in d:
			d[w]+=1
		else:
			d[w]=1

for key in sorted(d):
	print("{:s} : {:d}".format(key,d[key]))