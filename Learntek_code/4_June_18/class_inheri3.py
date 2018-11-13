class A():
	def sum1(self,a,b):
		c = a+b
		return c
		

class B(A):
	def sum1(self,a,b):
		c = a+b+10
		return c
		

obj = B()
print B.__dict__
print obj.sum1(6,4)
