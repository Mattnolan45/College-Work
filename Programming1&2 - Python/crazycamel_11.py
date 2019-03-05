import sys
lines=sys.stdin.readlines()

for line in lines: 
	line=line.split()
	s=""
	for word in line:
		last=word[-1]
		word=word[:-1]+last.capitalize()
		s+= word+" "	
	print(s.strip())