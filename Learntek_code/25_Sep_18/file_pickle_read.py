import pickle

file_r = open("file1.txt", "rb")

a = pickle.load(file_r)
print (a)