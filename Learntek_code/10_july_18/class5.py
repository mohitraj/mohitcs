class Learntek( ):

	inc_factor = 1.20
	
	def __init__(self,name ,lname , pay):
		
		self.name = name     # instance variable 
		self.lname = lname 
		self.pay = pay
		self.full_name =name +lname
		print self.full_name

	
	def make_email(self) :   # Regular Method 
		self.email = self.name+self.lname+"@learntek.com"      # Instance variable

		return self.email
		
	def increament(self):
		self.pay_amt = self.pay*self.inc_factor
		return self.pay_amt
	
	
class Instructor(Learntek) :
	def __init__(self,name ,lname , pay, subject):
		Learntek.__init__(self,name ,lname , pay)
		self.subject= subject
	
obj1 = Instructor("Mohit", "Raj", 60000, "Python")  # Object = Instance 
obj2 = Instructor("Bhaskar", "Das", 70000, "Java")


print obj1.subject

print obj2.subject



print obj1.full_name

print obj2.full_name

print obj1.make_email()

print obj2.make_email()

print obj1.increament()

print obj2.increament()



