import sys
import string


def main():
    letters=[]
    for word in sys.stdin.readlines():
        word=word.strip(string.punctuation)
        for l in word.strip():
            if l not in letters:
               letters.append(l)
    for a in letters:
        print(a)
        
if __name__=="__main__":
     main()

