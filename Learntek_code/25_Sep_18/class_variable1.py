class LearnTek():
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
		
obj1 = LearnTek('Mohit','raj',70000)
obj2 = LearnTek("Bhaskar",'Das', 60000)
obj1.inc_factor = 1.5
print (obj1.increment())
print (obj2.increment())

print (obj1.__dict__)
print ("\n")
print  (obj2.__dict__)
print ("\n")
print (LearnTek.__dict__)

print (LearnTek.emp_count)
