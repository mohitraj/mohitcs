class LearnTek():
	inc_factor = 1.4  # Class variable 
	inc_factor1 = 1.5
	def __init__(self, fname, lname, pay):  # Constructor 
		self.f_name = fname   # instance variables
		self.l_name= lname
		self.pay1= pay
		self.full_name = self.f_name+ self.l_name
		

		
	def email(self):   # Regular method
		self.Email =  self.full_name+"@LearnTek.com"
		self.full_name =  self.l_name+self.f_name
		
		return self.Email
		
	@staticmethod
	def rule1(amount):
		if amount <=50000:
			return True
		else :
			return False
		
	def increment(self):
		if self.rule1(self.pay1):
			self.inc_pay = self.inc_factor1*self.pay1
		else :
			self.inc_pay = self.inc_factor*self.pay1
		return self.inc_pay
		
	

		
		
obj1 = LearnTek('Mohit','raj',70000)
obj2 = LearnTek("Bhaskar",'Das', 40000)

print (obj1.increment())
print (obj2.increment())



