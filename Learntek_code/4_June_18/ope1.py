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
		
	def __add__(self,other):
		return self.pay+other.pay
		
	def __str__(self):
		return "This method belongs to "+ self.first_name
		
	def increment(self):   # Regular method
		self.pay = self.pay*self.inc_factor
		return self.pay
		
	def __gt__(self,other):
		a =self.pay< other.pay
		if a :
			statement = other.first_name+" Getting more"
		else :
			statement = other.first_name+" Getting less"
		return statement
	
	def __len__(self):
		self.full_name = self.first_name+self.last_name
		return len(self.full_name)
	
	
	
my_obj = xyz_org('Mohit','RAJ',30,70000)
my_obj1= xyz_org('Ravender','Dahiya',30,80000)

print my_obj
print my_obj1
print my_obj+my_obj1

print my_obj>my_obj1

print len(my_obj1)  # my_obj.__len__()


