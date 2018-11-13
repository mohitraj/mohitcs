tup1 = ((1,2,3),(1,2,6),(1,6,6,3),(1,2,7,3))

for each in tup1:
	if len(each)==3:
		a,b,c = each
		print a,b,c
		
		
"""
>>> tup3 = ((1,2,3,"Iron-man"))
>>> tup3 = ((1,2,3,"Iron-man"),78,90)
>>>
>>> tup3[0]
(1, 2, 3, 'Iron-man')
>>> tup3[0][3]
'Iron-man'
>>> tup3[0][3][5:]
'man'
>>>
"""