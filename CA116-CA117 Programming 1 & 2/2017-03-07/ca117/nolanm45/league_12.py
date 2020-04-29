import sys

teams=sys.stdin.readlines()
largest=0

for team in teams:
   team=( " ".join(team.split()[1:-8]))
   if len(team)>largest :
      largest=len(team)



print("{:3s} {:{}s}{:>3s}{:>4s}{:>4s}{:>4s}{:>4s}{:>4s}{:>4s}{:>4s}".format("POS","CLUB",largest,"P","W","D","L","GF","GA","GD","PTS"))


for team in teams:
    team=team.split()   
    print("{:>3s} {:{}s}{:>3s}{:>4s}{:>4s}{:>4s}{:>4s}{:>4s}{:>4s}{:>4s}".format(team[0]," ".join(team[1:-8]),largest,team[-8],team[-7],team[-6],team[-5],team[-4],team[-3],team[-2],team[-1]))  


