import sys
import string
lines=sys.stdin.read().casefold()

def sorter(t):
  return(t[1])

d={
  "a": 0, 
  "e": 0,
  "i": 0,
  "o": 0,
  "u": 0,
}

for w in lines:
    if w in d: 
       d[w]+=1

maxl=len(str(max(d.values())))


for (l,n) in sorted(d.items(), key=sorter, reverse=True):
    print("{:s} : {:>{}d}".format(l,n,maxl))
