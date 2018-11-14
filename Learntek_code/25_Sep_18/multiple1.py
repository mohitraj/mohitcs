class A():
	def sum(self, a,b):
		self.c = a+b
		print (self.c)
		
class B():
	def sum(self, a,b):
		self.c = a-b
		print (self.c)
		
class C(B,A):
	def sum(self,a,b):
		self.c = a*b
		print (self.c)
	
obj1 = C()

obj1.sum(10,20)
