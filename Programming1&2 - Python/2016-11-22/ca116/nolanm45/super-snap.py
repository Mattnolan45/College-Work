import sys

lines = sys.stdin.readlines()
seen = []

i = 0
while i < len(lines):
   if lines[i] not in seen:
      seen.append(lines[i])
   else:
      print "snap:",lines[i][:-1]
      i=i+len(lines)
   i = i + 1
