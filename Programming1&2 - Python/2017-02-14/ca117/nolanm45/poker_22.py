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
     rank=int(line[-2])
     if rank==0:
     	nothing+=1
     elif rank==1:
     	one+=1
     elif rank==2:
     	two+=1
     elif rank==3:
     	three+=1
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

print("The probability of nothing is {:.4f}%".format(nothing/len(lines)*100))
print("The probability of one pair is {:.4f}%".format(one/len(lines)*100))
print("The probability of two pairs is {:.4f}%".format(two/len(lines)*100))
print("The probability of three of a kind is {:.4f}%".format(three/len(lines)*100))
print("The probability of a straight is {:.4f}%".format(straight/len(lines)*100))
print("The probability of a flush is {:.4f}%".format(flush/len(lines)*100))
print("The probability of a full house is {:.4f}%".format(full/len(lines)*100))
print("The probability of four of a kind is {:.4f}%".format(four/len(lines)*100))
print("The probability of a straight flush is {:.4f}%".format(straightflush/len(lines)*100))
print("The probability of a royal flush is {:.4f}%".format(royal/len(lines)*100))

