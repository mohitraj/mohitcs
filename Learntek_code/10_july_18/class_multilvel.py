class A():
	def sum1(self,a,b):
		c = a+b
		return c
		
class B(A):
	pass
	
class C(B):
	pass
	
obj1 = C()
print obj1.sum1(12,3)

	