class Employee(object):

	next_employee_number=0
	def __init__(self,name,hourly_rate=9.25,hours_worked=0):
		self.name=name
		self.employee_number=Employee.next_employee_number
		self.hourly_rate=hourly_rate
		self.hours_worked=hours_worked
		Employee.next_employee_number+=1

	def add_hours(self,other):
		return self.hours_worked+other

	def __str__(self):
		return "Name: {}\nID: {}\nHours: {:.2f}\nRate: {:.2f}\nWages: {:.2f}\n".format(self.name,self.employee_number,self.hours_worked,self.hourly_rate,(self.hourly_rate*self.hours_worked))