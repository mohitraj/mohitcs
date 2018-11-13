class A():
	def sum1(self,a,b):
		c = a+b
		return c
		
class B(A):
	def sum1(self,a,b):
		c = a*b
		return c
		
		
obj1 = B()

print obj1.sum1(12,3)