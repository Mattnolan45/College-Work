
import sys
words = sys.stdin.read().split()

i = 0
while i < len(words):
   word = words[i]
   if word[0] == "-":
      word = word[1:]

   ds = word.split(".")
   if len(ds) == 1:
      ds.append("0")

   if len(ds) == 2 and ds[0].isdigit() and ds[1].isdigit():
      print words[i]
   i = i + 1
