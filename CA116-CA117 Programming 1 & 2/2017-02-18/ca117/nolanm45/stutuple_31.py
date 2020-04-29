from collections import namedtuple
Student=namedtuple('Student', ['firstname', 'surname' , 'id'])


def show_student(s):
	print("First name: {}".format(s.firstname))
	print("   Surname: {}".format(s.surname))
	print("        ID: {}".format(s.id))






