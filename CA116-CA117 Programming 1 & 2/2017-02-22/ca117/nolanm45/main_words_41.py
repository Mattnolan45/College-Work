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

maxl=len(max([k for k in sorted(d) if len(k)>3 and int(d[k])>=3],key=len))
maxl2=len(str(max([d[n] for n in sorted(d) if len(n)>3 and int(d[n])>=3])))

for key in sorted(d):
    if len(key)>3 and int(d[key])>=3:
        print("{:>{:d}s} : {:{:>d}}".format(key,maxl,d[key],maxl2))

