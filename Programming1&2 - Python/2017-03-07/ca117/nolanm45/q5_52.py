import sys

def standard_deviation(nums):
    N=len(nums)
    mean=float(sum(nums)/len(nums))
    m=[]
    for n in nums:
        m.append(float((n-mean))**2)
    return((sum(m)*1/(N-1))**0.5)


def main():
    nums=[int(n) for n in sys.stdin]
    print("Standard deviation: {:.3f}".format(standard_deviation(nums)))
 


if __name__=="__main__":
     main()
