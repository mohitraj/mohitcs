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
		
obj1 = LearnTek('Mohit','raj',70000)
obj2 = LearnTek("Bhaskar",'Das', 60000)

print (obj1.email())
print (obj2.email())

print (LearnTek.email(obj1))


print (obj1.full_name)

print (obj2.full_name)
'''

'''
obj1.f_name= "Mohit"  # instance variables 
obj1.l_name = "Raj"
obj1.pay = 70000

obj2.f_name= "Bhaskar"  # instance variables 
obj2.l_name = "Das" 
obj2.pay = 60000
'''