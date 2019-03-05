import sys   
n=sys.stdin.readline()

names={}


i=1
while 0<len(n):
	b=n.split()[3]
	if b not in names: 
		names[b]=("user-"+str(i))
		i+=1

	line=n.replace(b,names[b]).strip()
	sys.stdout.write(line+"\n")
	n=sys.stdin.readline()
   
    
    