import sys
lines=sys.stdin.readlines()

for line in lines:
     line=line.lower().split()
     new="" 
     for word in line: 
         if not word.isalnum():
            word=word[:-1]
         new+=word
     if new[0:]==new[::-1]:
        print(True)
     else:
        print(False)

