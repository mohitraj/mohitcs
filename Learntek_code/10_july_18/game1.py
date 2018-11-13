def toggle(bit):
	if bit =='0':
		return '1'
	else :
		return '0'

def first_case(main, left):
	list1 = []
	lnum = left
	if left== main:    # 2nd case 
		lnum = toggle(left)
	num = toggle(main)
	list1.append(lnum)
	list1.append(num)
	return list1
		
def second_case(main, right):
	list1 = []
	rnum = right
	if right== main:    # 2nd case 
		rnum = toggle(right)
	num = toggle(main)
	list1.append(num)
	list1.append(rnum)
	return list1
	
def Game1():	
	r = int(raw_input("Enter the Round\t"))
	n = int(raw_input("number by zita\t"))
	original_binary_num= bin(n)[2:]
	#print original_binary_num
	p = len(original_binary_num)
	original_binary_num1  = list(original_binary_num)
	original_binary_num = list(original_binary_num)
	turn = 0
	new_numnber = ""
	list1 =[]
	for round in xrange(r):
		turn = 0
		for move in xrange(p):
			turn = turn+1
			if move ==0 and p==1:
				new_numnber1 = toggle(original_binary_num[move])
				#print new_numnber1
			elif move==0 and move !=p-1:
				list1=second_case(original_binary_num[move], original_binary_num[move+1])
				original_binary_num[move]= list1[0]
				original_binary_num[move+1]= list1[1]
				if original_binary_num1 ==original_binary_num:
					break
			elif move >0 and move !=p-1:
				
				list2=first_case(original_binary_num[move], original_binary_num[move-1])
				list3=second_case(original_binary_num[move], original_binary_num[move+1])
				list2.append(list3[1])
				original_binary_num[move-1] =list2[0]
				original_binary_num[move] =list2[1]
				original_binary_num[move+1] =list2[2]
				#print "ori", original_binary_num
				if original_binary_num1 ==original_binary_num:
					break
				
			elif move ==p-1:
				#print "ori", original_binary_num
				list4=first_case(original_binary_num[move], original_binary_num[move-1])
				
				original_binary_num[move-1] =list4[0]
				original_binary_num[move] =list4[1]
				#print "ori", original_binary_num
				if original_binary_num1 ==original_binary_num:
					break
				
		
		if turn%2 ==1:
			return  "X"
		else :
			return "Y"
			
print Game1()