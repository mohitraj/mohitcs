from collections import namedtuple

emp2 = namedtuple("Game",['name', 'Skill', 'age'], rename = False)  # _0

record = emp2("Mohit", "Python", 30)

print record, type(record)


print record.name
print record.Skill

list1 = ["Manish", "JAVA", 28]


record2 = emp2._make(list1)

print record2._asdict()


record=  record._replace(age=25)

print record
