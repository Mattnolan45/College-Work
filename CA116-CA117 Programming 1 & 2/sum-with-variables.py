import sys

lines=sys.stdin.readlines()
total=0
i=0
while i<len(lines):
	line=lines[i].split()
	if line[i].isdigit():
		total=total+line[i]
     