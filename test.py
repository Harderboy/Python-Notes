#!/usr/bin/python3

dict = {'Name': 'Runoob', 'Age': 27}

print ("Age 值为 : %s" %  dict.get('Age'))
print ("Sex 值为 : %s" %  dict.get('Sex', "NA"))
print(dict.get('Sex'))
print(dict['Age'])

a = 0 or 1
print(a)
