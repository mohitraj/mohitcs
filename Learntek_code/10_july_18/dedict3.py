from collections import defaultdict


list1 = ['a','b','c','d','a','b','c','a']
game = defaultdict(int)
print game

for each in list1:
	game[each]= game[each]+1
	print each,":", game[each]

print game