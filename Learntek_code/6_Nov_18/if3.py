'''condition 
if student above 90 give A
if less than 90 but greater than 80 means B 
if less than 80 but greater than 60 means C 
if less than 60 means D
'''

grade =''

num1 = int(input("Enter the marks "))

if num1>= 90:
	grade = 'A'
elif num1 >=80:
	grade = "B"
elif num1 >= 60:
	grade ="C"
else :
	grade= "D"

print ("Grade is %s"%(grade))