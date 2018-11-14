import pickle

dict1= {}

dict1['names'] = ["Mohit", "Ravi", "manish"]
dict1['skills'] = ["Python","java", "java"]

file_w = open("file1.txt", "wb")


pickle.dump(dict1,file_w )


file_w.close()
