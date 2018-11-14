# Class method as A Alternative constructor 

class LearnTek():
	inc_factor = 1.4  # Class variable 
	
	def __init__(self, fname, lname, pay):  # Constructor 
		self.f_name = fname   # instance variables
		self.l_name= lname
		self.pay1= pay
		self.full_name = self.f_name+ self.l_name
		print (self.full_name)

		
	def email(self):   # Regular method
		self.Email =  self.full_name+"@LearnTek.com"
			
		return self.Email
		
	def increment(self):
		self.inc_pay = self.inc_factor*self.pay1
		return self.inc_pay
		
	@classmethod
	def inc_factor_change(cls, amount):
		cls.inc_factor = amount
		
	@classmethod
	def from_string(cls,str1):
		a,b,c = str1.split(",")
		obj1 =  cls(a,b,c)
		return obj1
		

str1 = "Mohit,Raj,70000"



#obj1 = LearnTek('Mohit','raj',70000)

obj1=LearnTek.from_string(str1)  #cls(a,b,c)
print (obj1.email())

print (LearnTek.email(obj1))





