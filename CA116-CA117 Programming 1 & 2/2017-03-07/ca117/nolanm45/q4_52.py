import sys

def build_dictionary(filename):
    d={}
    with open(filename,"r") as f:
          for line in f:
                 line=line.split()
                 d[" ".join(line[0:-1])]=line[-1]
    return(d)

def main():
    lines= [line.strip().split(",") for line in sys.stdin]
    cals=build_dictionary(sys.argv[1])
    total={}
    for person in lines:
        cal_count=0
        for food in person[1:]:
            if food in cals:
               cal_count+= int(cals[food])
            else:
               cal_count+=100 
        total[person[0]] = cal_count
    
    namew=len(max([n for n in sorted(total.keys())],key=len))
    calw=len(max([str(cal) for cal in sorted(total.values())],key=len))
    
    for key in sorted(total, key=total.get):
        print("{:>{:d}s} : {:>{:d}}".format(key,namew,total[key],calw))      


if __name__=="__main__":
     main()



