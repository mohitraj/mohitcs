import  collections 

co = collections.Counter([1,2,3,4,5,1,2,1,2,4,5,2,4,2,4])
print (co)

co1 = collections.Counter("Learntek Python Programming")


co1.update('india')
#co1.update({'a':4,'M': 4   })

print (co1)

print co1[' ']
