class Learntek( ):

	inc_factor = 1.20   # class variable
	inc_factor1 = 1.4

	
	def __init__(self,name ,lname , pay):
		
		self.name = name     # instance variable 
		self.lname = lname 
		self.pay = pay
		self.full_name =name +lname
		#print self.full_name

	
	def make_email(self) :   # Regular Method 
		self.email = self.name+self.lname+"@learntek.com"      # Instance variable

		return self.email
		
	@classmethod
	def inc_factor_set(cls,amt):
		cls.inc_factor = amt
	

		
	def increament(self):
		if self.ispayment_inc(self.pay):
			self.pay_amt = self.pay*self.inc_factor1
		else :
			self.pay_amt = self.pay*self.inc_factor
		return self.pay_amt
		
	@staticmethod
	def ispayment_inc(pay):
		if pay< 50000:
			return True
		else :
			return False
	
	
obj1 = Learntek("Mohit", "Raj", 60000)  # Object = Instance 

obj2 = Learntek("Bhaskar", "Das", 40000)  # Object = Instance 



print "Incremented amount is ", obj1.increament()

print "Incremented amount is ", obj2.increament()

	