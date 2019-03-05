import sys

def main():
	nums=[int(n.strip()) for n in sys.stdin]

	mean=sum(nums)/len(nums)
	mid=len(nums)/2
	if len(nums)%2==0:
		median=float((sorted(nums)[mid])+(sorted(nums)[mid+1]))
	else:
		median=float(sorted(nums)[mid])
	total=0
	m=0
	for n in nums:
		if nums.count(n)<total:
			total=nums.count(n)
			m=n
	mode=m
	print("Mean: {}".format(mean))
	print("Median: {}".format(median))
	print("Mode: {}".format(mode))

if __name__=="__main__":
	main()
