import sys
from math import sqrt
 
 
def main():
        for line in sys.stdin:
            try:
               line=line.strip().split()
               a,b,c=int(line[0]),int(line[1]),int(line[2])
               r1=(-b+sqrt((b**2)-(4*a*c)))/(2*a)
               r2=(-b-sqrt((b**2)-(4*a*c)))/(2*a)
               print("r1 = {}, r2 = {}".format(r1,r2))
            except:
               print("None")


if __name__=="__main__":
     main()


