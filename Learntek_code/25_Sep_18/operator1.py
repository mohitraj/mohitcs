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
		
	def __add__(self,other):
		c =  self.f_name+other.f_name
		return c 
		
	def __len__(self):
		return (len(self.full_name))
		
	def __gt__(self,other):
		return self.pay> other.pay
		
	def __str__(self):
		return ("This is the object of LearnTek")
		
		
obj1 = LearnTek('Mohit','raj',70000)
obj2 = LearnTek("Bhaskar",'Das', 80000)

print (dir(obj1))

print (obj1+obj2)

print (len(obj2))


print (obj1>obj2)

print (obj1)

# LearnTek.__add__(obj1,obj2)