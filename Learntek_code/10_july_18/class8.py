class Learntek( ):

	inc_factor = 1.20
	emp_count = 0
	
	def __init__(self,name ,lname , pay):
		
		self.name = name     # instance variable 
		self.lname = lname 
		self.pay = pay
		self.full_name =name +lname
		#print self.full_name
		Learntek.emp_count=  Learntek.emp_count+ 1
	
	def make_email(self) :   # Regular Method 
		self.email = self.name+self.lname+"@learntek.com"      # Instance variable

		return self.email
		
	def __add__(self,other):
		#return self.pay+ other.pay   # int.__add__(self.pay,other.pay)
		return self.name + other.name  # str.__add__(self.name, other.name)
	
	def __gt__(self,other):
		return self.pay> other.pay
		
	def __str__(self):
		str1 = "Class name is Learntek"
		return str1
	
	def __len__(self):
		len1 = len(self.full_name) # str.__len__(self.full_name)
		return len1

	
	
obj1 = Learntek("Mohit", "Raj", 60000)  # Object = Instance 
obj2 = Learntek("Bhaskar", "Das", 70000)

print obj1+obj2  # 60000+70000  = 130000
print obj1
print obj1>obj2

print len(obj1)




