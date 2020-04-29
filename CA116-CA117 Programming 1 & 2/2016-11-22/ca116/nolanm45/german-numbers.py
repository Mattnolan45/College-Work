import sys
lines=sys.stdin.readline().strip()

n={
  "one":"eins",
  "two":"zwei",
  "three":"drei",
  "four":"vier",
  "five":"funf",
  "six":"sechs",
  "seven":"sieben",
  "eight":"acht",
  "nine":"neun",
  "ten":"zehn",
}

i=0
while i<len(lines):
  if lines in n:
     sys.stdout.write(n[lines]+"\n")
  lines=sys.stdin.readline().strip()
