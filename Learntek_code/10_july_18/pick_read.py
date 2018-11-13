import cPickle 

pick = open("data1.txt",'r')

data = cPickle.load(pick)




print data.get('Company')


pick.close()

