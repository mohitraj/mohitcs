class LearnTek():
	def __init__(self, fname, lname, pay):  # Constructor 
		self.f_name = fname   # instance variables
		self.l_name= lname
		self.pay= pay
		self.full_name = self.f_name+ self.l_name
		print (self.full_name)
		
	def email(mohit):   # Regular method
		mohit.Email =  mohit.full_name+"@LearnTek.com"
		return mohit.Email
	@classmethod
	def from_string(cls, str1):
		a,b,c =  str1.split()
		#LearnTek('Mohit','raj',70000)
		return cls('Mohit','raj',70000)
		
str1 = "Mohit Raj 70000"		
		


#obj1 = LearnTek(a,b,c)
#obj1 = LearnTek('Mohit','raj',70000)

LearnTek.from_string(str1)
