import sys

lines=sys.stdin.readlines()
i=0
while i<len(lines):
    line=lines[i].split()   
    print len(line)
    i+=1
