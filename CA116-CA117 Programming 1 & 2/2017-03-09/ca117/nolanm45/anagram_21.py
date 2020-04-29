import sys

[print(sorted(w1)==sorted(w2)) for line in sys.stdin for w1,w2 in [line.split()]]
