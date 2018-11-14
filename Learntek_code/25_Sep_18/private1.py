class A:
	__amount = 45   #Private variable
	def __info(self):  # Private method
		print ("I am in Class A")
	def hello(self):
		print ("Amount is ",A.__amount)
		self.__info()

		
a = A()
a.hello()

a._A__info()
print (a._A__amount)
