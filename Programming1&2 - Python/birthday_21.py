import sys
import calendar

day = calendar.weekday(int(sys.argv[3]), int(sys.argv[2]), int(sys.argv[1]))

days = {
   0: "Monday",
   1: "Tuesday",
   2: "Wednesday",
   3: "Thursday",
   4: "Friday",
   5: "Saturday",
   6: "Sunday"
}

rhyme = {
   "Monday": "Monday's child is fair of face.",
   "Tuesday": "Tuesday's child is full of grace.",
   "Wednesday": "Wednesday's child is full of woe.",
   "Thursday": "Thursday's child has far to go.",
   "Friday": "Friday's child is loving and giving.",
   "Saturday": "Saturday's child works hard for a living.",
   "Sunday": "Sunday's child is fair and wise and good in every way."
}

print("You were born on a", days[day], "and", rhyme[days[day]])

