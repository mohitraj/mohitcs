class LearnTek():
	inc_factor = 1.4  # Class variable 
	
	def __init__(self, fname, lname, pay):  # Constructor 
		self.f_name = fname   # instance variables
		self.l_name= lname
		self.pay1= pay
		self.full_name = self.f_name+ self.l_name
		

		
	def email(self):   # Regular method
		self.Email =  self.full_name+"@LearnTek.com"
		self.full_name =  self.l_name+self.f_name
		
		return self.Email
		
	def increment(self):
		self.inc_pay = self.inc_factor*self.pay1
		return self.inc_pay
		
	@classmethod
	def inc_factor_change(cls, amount):
		cls.inc_factor = amount
		
		
obj1 = LearnTek('Mohit','raj',70000)
obj2 = LearnTek("Bhaskar",'Das', 60000)

LearnTek.inc_factor_change(1.5)
print (LearnTek.inc_factor)
print (obj1.inc_factor)


