# num <=90 greade A   
# num > 90  greater 70  B

# num > 60  less than 70 C
#less than 60 means D


num1 = int(input("Enter the number :"))



grade = ""
if num1>=90:
	grade = "A"
elif num1>=70 and num1<90:
	grade = "B"
elif num1 >=60 and num1<70:
	grade = 'C'
	
else :
	grade = "D"
	
print ("Grade is "+grade)