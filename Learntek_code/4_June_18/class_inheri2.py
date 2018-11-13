class A():
	def sum1(self,a,b):
		c = a+b
		return c
		

class B():
	def sum1(self,a,b):
		c = a*b
		return c
		
class C(A,B):
	pass
	
obj = C()

print obj.sum1(6,4)
#print obj.mul1(3,4)