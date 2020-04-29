import sys
p={}


with open("contacts_long.txt","r") as contacts:
    for line in contacts:
        line=line.strip().split()
        p[line[0]]=line[1],line[2]
     

names=sys.stdin.readlines()
for name in names:
    name=name.strip() 
    print("Name: {}".format(name))
    try:
        print("Phone: {}".format(p[name][0]))
        print("Email: {}".format(p[name][1]))
    except:
       
          print("No such contact")
