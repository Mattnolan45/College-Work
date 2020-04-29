import sys
words=sys.stdin.read().split()

i=0
while i<len(words):
   word=words[i]

   if word[0]=="-":
      word=word[1:]
   
   if word.isdigit():
      print words[i]
   i+=1
