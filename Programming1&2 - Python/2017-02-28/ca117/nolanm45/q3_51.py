import sys

def main():
       d={
          "January":"1",
          "February":"2", 
          "March":"3",
          "April":"4",
	  "May":"5",
          "June":"6",
          "July":"7",
          "August":"8",
          "September":"9",
          "October":"10",
          "November":"11",
          "December":"12",
          }
       for date in sys.stdin:
              date=date.split()
              print(date[0]+"/"+d[date[1]]+"/"+date[2][2:])


if __name__ == "__main__":
     main()
