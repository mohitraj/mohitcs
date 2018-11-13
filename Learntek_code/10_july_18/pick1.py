import cPickle 

dict1  = {}

dict1['name'] = ["Mohit","Ravender", "Bhaskar"]

dict1['skill'] = ["Python", "Machine learning", "JAVA"]

dict1['Company'] = ["Sapient", "Delliot", "IBM"]

pick = open("data1.txt", "w")

cPickle.dump(dict1,pick)


pick.close()





