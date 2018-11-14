import collections

de = collections.deque("Mohitraj")

print (de)

print (de[0])

print (de[-1])

print (len(de))

# Populating the values meand adding the values

#de.append("Skill")


de.extend("skill")
print (de)


de.appendleft("hello")

print (de)

