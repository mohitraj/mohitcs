i=8
class xyz_org():
	inc_factor = 1.25   # class variable 
	emp_count = 0      # class variable 
	def __init__(self,name,l_name,age,pay):  #constructor
		self.first_name = name # instance varible 
		self.last_name = l_name
		self.age = age
		self.pay = pay
		xyz_org.emp_count = xyz_org.emp_count+1    
		
	
	def make_email(self):    # Regular method
		self.email = self.first_name+self.last_name+"@xyz.com" 
		return self.email
		
	def increment(self):   # Regular method
		self.pay = self.pay*self.inc_factor
		return self.pay
		
class instructor(xyz_org):     #child class, derived class
	def __init__(self,name,l_name,age,pay, subject):
		xyz_org.__init__(self,name,l_name,age,pay)
		self.subject = subject 
		self.inc_factor = 1.35
		






	
my_obj = instructor('Mohit','RAJ',30,70000,"Python")
my_obj1= instructor('Ravender','Dahiya',30,80000, "Data Science")



print "Subject is ", my_obj.subject
print "Subject is ", my_obj1.subject
print my_obj.increment()
print my_obj1.increment()


