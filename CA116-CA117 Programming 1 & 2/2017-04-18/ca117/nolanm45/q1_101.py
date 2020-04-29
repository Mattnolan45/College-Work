import sys

def main():
    print(rotate(str(sys.argv[1]),int(sys.argv[2])))

def rotate(s, n):
  return s[-n % len(s):] + s[:-n % len(s)]
    
if __name__=="__main__":
     main()
