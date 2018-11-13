>>> str1.ljust(20,"$")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'str1' is not defined
>>>
>>> str1  = "Python"
>>> str1.ljust(20,"$")
'Python$$$$$$$$$$$$$$'
>>> str1.rjust(20,"$")
'$$$$$$$$$$$$$$Python'
>>>
>>> str1.cetre(20,"$")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'cetre'
>>> str1.centre(20,"$")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'centre'
>>> str1.center(20,"$")
'$$$$$$$Python$$$$$$$'
>>>
>>>
>>> str1.center(3,"#")
'Python'
>>> str1.center(9,"#")
'##Python#'
>>>
>>> str1
'Python'
>>>
>>> str1.ljust(3,"$")
'Python'
>>> str1.ljust(8,"$")
'Python$$'
>>>
>>>
>>> str1
'Python'
>>>
>>>
>>> str1.zfill(10)
'0000Python'
>>> str1.rjust(10,"0")
'0000Python'
>>>
>>>
>>> 12
12
>>>
>>> bin(12)
'0b1100'
>>> bin(12)[2:]
'1100'
>>> bin(32)[2:]
'100000'
>>>
>>>
>>> bin(32)[2:].zfill(8)
'00100000'
>>>
>>> bin(1)[2:].zfill(8)
'00000001'
>>> bin(15)[2:].zfill(8)
'00001111'
>>>
>>>
>>>
>>> str4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'str4' is not defined
>>> str4 = "$$Python $ Learning $$"
>>>
>>>
>>> str4
'$$Python $ Learning $$'
>>>
>>> str4.strip("$")
'Python $ Learning '
>>>
>>>
>>> str4
'$$Python $ Learning $$'
>>>
>>>
>>> str4.replace("$","")
'Python  Learning '
>>> str4.replace("$","-")
'--Python - Learning --'
>>>
>>>
>>> str4.replace("$"," ")
'  Python   Learning   '
>>> str4.replace("$","")
'Python  Learning '
>>>
>>>
>>> str4.replace("$","").replace(" ", "")
'PythonLearning'
>>>
>>>
>>> str4.replace("$","",1)
'$Python $ Learning $$'
>>> str4.replace("$","-",1)
'-$Python $ Learning $$'
>>> str4.replace("$","-",3)
'--Python - Learning $$'
>>> str4.replace("$","-")
'--Python - Learning --'
>>>
>>>
>>> date1 = "11-09-2018"
>>>
>>> date1
'11-09-2018'
>>>
>>>
>>> date1.split("-")
['11', '09', '2018']
>>> list1 =date1.split("-")
>>>
>>> list1
['11', '09', '2018']
>>>
>>>
>>> "-".join(list1)
'11-09-2018'
>>>
>>> "/".join(list1)
'11/09/2018'
>>>
>>>
>>> date1
'11-09-2018'
>>>
>>>
>>> "/".join(  date1.split("-")  )
'11/09/2018'
>>>




