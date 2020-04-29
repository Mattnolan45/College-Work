import sys


def insertion_sort(lst):
	swapcount=0
	comparecount=0
	for todo in range(1, len(lst)):
		tobeinserted = lst[todo]
		i = todo
        while i > 0 and tobeinserted < lst[i-1]:
            lst[i] = lst[i-1] # Make space for the item
            i -= 1
            swapcount+=1
        if i>0:
        	comparecount+=1
        lst[i] = tobeinserted  # Found the place for this item, plonk it in
        return comparecount+swapcount, swapcount

def main():
    # Read each test case
    line = sys.stdin.readline()
    items = line.strip().split()
    
    orig = list(items)

    result = insertion_sort(items)
    if items != sorted(orig):
        print("The list is not sorted.")
    else:
        print(result)

if __name__ == "__main__":
    main()