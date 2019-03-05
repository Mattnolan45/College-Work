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
    for w in sys.stdin.readlines():
        w=w.split()
        times=w[2:]
        best_time=1000
        for t in times:
            if mins_to_secs(t)<best_time:
               best_time=int(mins_to_secs(t))
               time=t
               name=w[0]
    print("{} : {}".format(name,":".join(time)))
            
        



if __name__=="__main__":
    main() 
    
