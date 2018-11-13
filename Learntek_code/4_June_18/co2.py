import collections

co1 = collections.Counter("it is not easy to play another man's game")

print co1
for each in "aeuio":
	print each, " : ", co1[each]
	