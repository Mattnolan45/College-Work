import sys

lines="".join(sys.stdin.read().split())
for c in [char for char in lines if lines.count(char)==1]:
      print(c)
