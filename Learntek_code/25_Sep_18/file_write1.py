import os

list1 = ["Hello everyone good Evening\n","This is a python class\n","peace being with smile\n "]

file_w = open("class1.txt", "w")

file_w.writelines(list1)



file_w.close()