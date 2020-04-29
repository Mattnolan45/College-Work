import sys
lines=sys.stdin.readline().strip()


fruit = {
   "apple": True,
   "pair": True,
   "orange": True,
   "banana": True,
   "cherry": True,
}


i=0
while i<len(lines):
   if lines in fruit:
      sys.stdout.write(lines+"\n")
   lines=sys.stdin.readline().strip()

