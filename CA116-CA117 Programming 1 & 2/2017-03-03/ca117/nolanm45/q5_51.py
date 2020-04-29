import sys

def mins_to_secs(t):
    t=t.split(":")
    try:
       minute=int(t[0])
       seconds=int(t[1])
       return(minute*60 + seconds)
    except:
         pass
  

def main():
    d={}
    for line in sys.stdin.readlines():
         line=line.strip()
         d[line[0]]=min(line[1:],key=lambda(X:d[x])
    print d
        



if __name__=="__main__":
    main() 
    
