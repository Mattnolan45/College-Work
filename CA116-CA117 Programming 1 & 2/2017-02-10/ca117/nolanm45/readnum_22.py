import sys

for line in sys.stdin: 
    try: 
      line=int(line)
      print(("Thank you for {}").format(line))
      break
    except ValueError:
      print(("{} is not a number").format(line.strip()))
