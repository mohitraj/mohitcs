from collections import defaultdict

def fun1():
	return "Cricket"

game = defaultdict(fun1)


game["Ankur"] = "Badminton"
game['Bhaskar'] = "Football"
print (game["Ankur"])
print (game['Mohit'])
print (game['jay'])

print (game)

