import sys
score= int(sys.argv[1])
goals=0
points=score
i=0
while i<10:
  points=score-3*goals
  if points < 0:
     i=i+20
  else:
     print goals,points
  goals= goals+1
 
  






 


