import math
import logger1 as lg

list1 = [1,2,34,6,'',75,6,4,6,3,53,5]

#legend method

for num1 in list1:

	flag = 1
	try:
		num2 = int(math.sqrt(num1))+1
	except Exception as e :
		lg.logger.error(e)

	for each in range(2,num2):
		try:
			c = num1%each
			if c==0:
				flag =0
				
				lg.logger.info('"divisible by : {0} '.format(each))
				break
		except Exception as e :
			lg.logger.error('Error in : {0} {1}'.format(c,e))
		
	if flag==1:
		
		lg.logger.info('Number is prime : {0}'.format(num1))
		
	else :
		
		lg.logger.info('Number is not prime : {0}'.format(num1))
		
		
		
		