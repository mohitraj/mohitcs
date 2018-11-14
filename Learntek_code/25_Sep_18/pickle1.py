import pickle

names = ["Mohit", "Ravi", "manish"]
skills = ["Python","java", "java"]

file_w = open("file1.txt", "wb")


pickle.dump(names,file_w )
pickle.dump(skills,file_w )

file_w.close()
