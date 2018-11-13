import os
a =  os.popen("ping google.com")
text =  a.read()

index1 = text.find('statistics')
print index1

print text[index1:]