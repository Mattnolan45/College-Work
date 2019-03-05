import sys

def main():
	nums=[int(n.strip()) for n in sys.stdin]

	mean=sum(nums)/len(nums)
	
	mid=int(len(nums)/2)
	if len(nums)%2==0:
		median=float(((sorted(nums)[mid])+(sorted(nums)[mid-1]))/2)
	else:
		median=float(sorted(nums)[mid])
	
	total=0
	m=0
	for n in nums:
		if nums.count(int(n))>total:
			total=nums.count(int(n))
			m=n
	mode=m
	
	print("Mean: {:.1f}".format(mean))
	print("Mode: {:.1f}".format(mode))
	print("Median: {:.1f}".format(median))



if __name__=="__main__":
	main()
