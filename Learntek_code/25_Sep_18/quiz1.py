def fun1(a, list1=[]):
	list1.append(a)
	print(a,list1 )  # 12,[12]    fun1(12)
					  #  13, [13]   fun1(13)
	
fun1(12)
fun1(13,[])
fun1(56)