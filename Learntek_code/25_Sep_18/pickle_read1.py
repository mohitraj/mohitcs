import pickle

file_r = open("file1.txt", "rb")

a = pickle.load(file_r)
print (a)

b = pickle.load(file_r)
print (b)



file_r.close()