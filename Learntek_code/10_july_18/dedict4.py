from collections import defaultdict


list1 = [("Haryana", "Karnal"), ("Haryana","YamunaNagar" ), ("Haryana", 'KUK'), ("Punjab", "CHD"), ("Punjab","Patiala"),("UP", "Noida")]

#print dict(list1)

state = defaultdict(list)

print state



for k,v in list1:
	print state[k].append(v)
	
print state