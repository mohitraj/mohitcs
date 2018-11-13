class my_class():
	inc_factor = 1.25   # Class variable 
	def __init__(self,name,age,pay):
		self.name = name    #instance variable
		self.age = age
		self.pay = pay
	def make_email(self):
		self.email = self.name+"@xyz.com"   #instance variable
		return self.email
		
	def increment(self):
		a = self.decide_in_factor(self.pay)
		print a
		if a:
			self.inc_factor = 1.4
			
		self.pay = self.pay*self.inc_factor     #instance variable
		
		print "Email is ",self.email
		return self.pay

	@staticmethod
	def decide_in_factor(amt):
		if amt<50000:
			return True
		else :
			return False




		
lobj = my_class("mohit",30,45000)
lobj1 = my_class('ravender', 30,80000)


print lobj.make_email()
print lobj.pay
print lobj.increment()


print lobj1.make_email()
print lobj1.pay
print lobj1.increment()