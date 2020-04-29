home_goals= input()
home_points=input()
away_goals= input()
away_points=input()

total_home= (home_goals*3)+home_points
total_away= (away_goals*3)+away_points

if total_home>total_away:
    print "home win"
elif total_away==total_home:
    print "draw"
elif total_away>total_home:
    print "away win"
