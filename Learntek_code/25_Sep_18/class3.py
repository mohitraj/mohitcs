class LearnTek():
	def __init__(self, fname, lname, pay):  # Constructor 
		self.f_name = fname   # instance variables
		self.l_name= lname
		self.pay1= pay
		self.full_name = self.f_name+ self.l_name
		print (self.full_name)
		print ("in init", self)
		
	def email(self):   # Regular method
		self.Email =  self.full_name+"@LearnTek.com"
		self.full_name =  self.l_name+self.f_name
		print ("in email", self.full_name)
		print ("self",self)
		print (self.pay1)
		return self.Email
		
	def testing(self):
		print ("Name is ", self.l_name)
		#print ("email is ",self.Email )
		print ("Full_name is ", self.full_name)
		
obj1 = LearnTek('self','raj',70000)
obj2 = LearnTek("Bhaskar",'Das', 60000)

print (obj1.email())
obj1.testing()

print ("outside ", obj1.Email)


print ("outside", obj1)