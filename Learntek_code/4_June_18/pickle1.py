import cPickle as p

dict1 = {}

dict1['name']=["Mohit","Ravi","Bhaskar"]

dict1['skill']=["Python","java","java"]

dict1['Company']=["Sapient","IBM","IBM"]


pickle_w = open("pick1.raj","w")

p.dump(dict1,pickle_w)

pickle_w.close()