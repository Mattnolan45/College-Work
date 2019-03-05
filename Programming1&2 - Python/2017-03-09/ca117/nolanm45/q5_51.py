import sys

   
def mins_to_seconds(t):
      [mins, secs] = t.split(":")
      totals = int(mins)*60 + int(secs)
      return(totals)
 
def main():
    d={}
    for line in sys.stdin:
       try:
          line=line.split()
          d[line[0]]=min(line[1:],key=mins_to_seconds)
       except ValueError: 
          continue
    d2={v:k for (k,v) in d.items()}        
    best_time=min(d2.keys(),key=mins_to_seconds)
    print("{} : {}".format(d2[best_time],best_time))
          


if __name__=="__main__":
    main() 
    
