import sys
n=int(sys.argv[1])+1

print("Multiples of 3: {}".format([c for c in range(1,n,1) if not c%3]))
print("Multiples of 3 squared: {}".format([c*c for c in range(1,n,1) if not c%3]))
print("Multiples of 4 doubled: {}".format([c*2 for c in range(1,n,1) if not c%4]))
print("Multiples of 3 or 4: {}".format([c for c in range(1,n,1) if not c%3 or not c%4]))
print("Multiples of 3 and 4: {}".format([c for c in range(1,n,1) if not c%3 and not c%4]))
print("Multiples of 3 replaced: {}".format([c if c%3 else "X" for c in range(1,n,1)]))
