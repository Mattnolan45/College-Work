import sys
pattern=sys.argv[1]

line=raw_input()
while line!= "end":
	i=0
	while i<len(line) and line[i:i+len(pattern)] != pattern:
		i+=1
		if i<len(line):
			print line
		line=raw_input()