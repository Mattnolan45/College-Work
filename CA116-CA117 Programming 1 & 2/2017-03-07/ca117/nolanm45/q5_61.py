import sys

def sorter(t):
    return t[1]



def main():
    d={}
    for line in sys.stdin:
        line=line.split()
        team=" ".join(line[0:-5]).strip(":")
        score=line[-5:]
        total=0
        try:
           for n in score:
              total+=int(n)
           d[team]=total
        except ValueError:
            pass
    teamw=len(max(d.keys(),key=len))
    scorew=len(str(max(d.values())))


    
    for k,v in sorted(d.items(),key=sorter,reverse=True):
         print("{:>{:d}s}: {:{:d}d} points".format(k,teamw,v,scorew))




if __name__=="__main__":
     main()
