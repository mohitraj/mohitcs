class Learntek( ):
	def __init__(self,name ,lname , pay):
		
		self.name = name     # instance variable 
		self.lname = lname 
		self.pay = pay
		self.full_name =name +lname
		print self.full_name
	
obj1 = Learntek("Mohit", "Raj", 60000)  # Object = Instance 
obj2 = Learntek("Bhaskar", "Das", 70000)








