class Learntek( ):
	def __init__(self,name ,lname , pay):
		
		self.name = name     # instance variable 
		self.lname = lname 
		self.pay = pay
		self.full_name =name +lname

		print self.full_name
		
	def make_email(self) :   # Regular Method 
		self.email = self.name+self.lname+"@learntek.com"      # Instance variable

		return self.email
		
	
	
	
	
obj1 = Learntek("Mohit", "Raj", 60000)  # Object = Instance 
#obj2 = Learntek("Bhaskar", "Das", 70000)




print obj1.make_email()

#print Learntek.make_email(obj1)

#print obj2.make_email()

