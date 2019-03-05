import sys
lines=sys.stdin.readlines()

for word in lines:
    word1=word.split()[0]
    word2=word.split()[1]
    if sorted(word1)== sorted(word2): 
       print(True)
    else:
       print(False)
    


