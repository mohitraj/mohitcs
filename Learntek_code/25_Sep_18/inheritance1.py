class A():
	def sum(self, a,b):
		self.c = a+b
		print (self.c)
		
class B(A):
	def sub1(self, a,b):
		self.c = a-b
		print (self.c)
		
class C(B):
	pass
	
obj1 = C()

obj1.sum(10,20)