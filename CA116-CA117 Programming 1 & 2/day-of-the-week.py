day = 2
is_college_day = day <6
is_weekend = day > 5
is_ca116_day = day > 1 or day < 5
is_not_ca116_day = day < 1 or day < 5

print "day is a college day",is_college_day
print "day is a weekend day:",is_weekend
print "day is a ca116 day:", is_ca116_day
print "day is not a ca116 day:",is_not_ca116_day

