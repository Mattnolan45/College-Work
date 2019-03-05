import sys


def standard_deviation(nums):
    N=len(nums)
    mean=sum(nums)/N
    m=[] 
    if N-1!=0:
      for n in nums:
          m.append((int(n)-mean)**2)
      return("Standard deviation: {:.3f}".format((1/(N-1)*sum(m))**0.5))
   
    else:
      return("Standard deviation: NaN")  


def main():
  
     nums=[int(n) for n in sys.stdin] 
     print(standard_deviation(nums))

if __name__=="__main__":
     main()
