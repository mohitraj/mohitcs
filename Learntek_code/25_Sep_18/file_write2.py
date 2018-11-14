import os



file_w = open("class1.txt", "w")

file_w.write("Peace being with smile \n")
file_w.write("Be yourself\n")


file_w1 = open("class1.txt", "a")
file_w1.write("Be111111 yourself\n")
file_w.close()

file_w1.close()