class LearnTek():   # base class, parent , general class
	inc_factor = 1.4
	emp_count = 0
	def __init__(self, fname, lname, pay):  # Constructor 
		self.f_name = fname   # instance variables
		self.l_name= lname
		self.pay1= pay
		self.full_name = self.f_name+ self.l_name
		LearnTek.emp_count = LearnTek.emp_count+1

		
	def email(self):   # Regular method
		self.Email =  self.full_name+"@LearnTek.com"
		self.full_name =  self.l_name+self.f_name
		
		return self.Email
		
	def increment(self):
		self.inc_pay = self.inc_factor*self.pay1
		return self.inc_pay
		
		
class Instructor(LearnTek):   # child class , drived , special 
	def __init__(self,fname, lname, pay, subject):
		LearnTek.__init__(self,fname, lname, pay)
		self.subject = subject
		print (self.f_name)
		print (self.subject)
		
obj1 = Instructor('Mohit','raj',70000,"Python")
obj2 = Instructor("Bhaskar",'Das', 60000, "java")

print (obj1.email())

print (obj2.email())
