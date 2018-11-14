from collections import defaultdict



game = defaultdict(lambda  : "Cricket")


game["Ankur"] = "Badminton"
game['Bhaskar'] = "Football"
print (game["Ankur"])
print (game['Mohit'])
print (game['jay'])

print (game)
