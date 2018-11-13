

marks = int(raw_input("Please enter the marks\t"))

grade = ""

if marks>89:
	grade = 'A'

elif marks > 70:
	grade = "B"
	
elif marks > 60:
	grade = 'C'
else :
	grade ='D'

print "Grade of the student is ", grade



