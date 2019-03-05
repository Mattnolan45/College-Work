line=raw_input()
while line!="end":
	s=""
	i=0
	while i <len(line):
		s=s+line[len(line)-1-i]
		i+=1
	print s	
	line=raw_input()
