dublin_goals = 2
dublin_points = 8

kerry_goals = 3
kerry_points = 5

total_dublin = (2*dublin_goals)+dublin_points
total_kerry = (2*kerry_goals)+kerry_points

if total_dublin > total_kerry :
  print "Dublin win"
elif total_kerry > total_dublin :
  print "Kerry win"
elif total_kerry == total_dublin :
  print "Draw"

