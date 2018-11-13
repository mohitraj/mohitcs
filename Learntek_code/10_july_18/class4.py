class Learntek( ):

	inc_factor = 1.20
	emp_count = 0
	
	def __init__(self,name ,lname , pay):
		
		self.name = name     # instance variable 
		self.lname = lname 
		self.pay = pay
		self.full_name =name +lname
		print self.full_name
		Learntek.emp_count=  Learntek.emp_count+ 1
	
	def make_email(self) :   # Regular Method 
		self.email = self.name+self.lname+"@learntek.com"      # Instance variable

		return self.email
		
	def increament(self):
		self.pay_amt = self.pay*self.inc_factor
		return self.pay_amt
	
	
obj1 = Learntek("Mohit", "Raj", 60000)  # Object = Instance 
obj2 = Learntek("Bhaskar", "Das", 70000)

obj3 = Learntek("Manish", "Das", 70000)


obj1.inc_factor= 1.3

print obj1.increament()

print obj2.increament()


print "Space of obj1 ",obj1.__dict__

print "Space of obj2 ",obj2.__dict__


print "Space of class ", Learntek.__dict__


print "Number of emp",  Learntek.emp_count



