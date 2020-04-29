import sys

def sumFac(num):
    return(sum([n for n in range(1,(int(num/2))+1,1) if num%n==0 ])) 
    
def isPerfect(num):
    if num==sumFac(num):
       return(True)
    else:
       return(False)


def main():
    for line in sys.stdin:
        print(isPerfect(int(line.strip())))
    

if __name__=="__main__":
     main()
    

