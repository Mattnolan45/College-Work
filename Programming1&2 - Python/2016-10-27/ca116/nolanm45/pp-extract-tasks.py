line = raw_input()
text=""


i=0
while i<len(line) and i!="+":
   i+=1
start = i+1

i=start 
while i<len(line) and line[i]!="+":
   i+=1

if i<len(line):
   text=len[start:i]

if text[len(text)-3:]== ".py" :
   print text 
