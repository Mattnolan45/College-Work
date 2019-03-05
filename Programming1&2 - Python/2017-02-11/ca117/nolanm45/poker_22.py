import sys
nothing=0
one=0
two=0
three=0
straight=0
flush=0
full=0
four=0
straightflush=0
royal=0



lines=sys.stdin.readlines()


for line in lines:
	rank=int(line[-1])
    if rank==0:
    	nothing+=1
    elif rank==1:
    	one+=1
    elif rank==2:
    	two+=1
    elif rank==3:
    	three+=3
    elif rank==4:
    	straight+=1
    elif rank==5:
    	flush+=1
    elif rank==6:
    	full+=1
    elif rank==7:
    	four+=1
    elif rank==8:
    	straightflush+=1
    elif rank==9:
    	royal+=1

print("The proabability of nothing is {}".format(nothing))

    