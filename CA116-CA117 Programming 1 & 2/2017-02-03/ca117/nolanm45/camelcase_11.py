import sys

a=sys.stdin.readline()
while 0<len(a):
    b=a.split()

    print(" ".join(c.capitalize() for c in b))
    a=sys.stdin.readline()
