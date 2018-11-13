#if more than 90 A
#if less 90 greater 80 B..

num = int(raw_input("Enter the number \t"))

grade = ''
if num>=90:
	grade= "A"
elif num<90 and num>=80:
	grade= 'B'

elif num<80 and num>60:
	grade="C"
else :
	grade="F"
	
print grade