import random
file1=open("dictionary.txt","r")
list1=[i.replace('\n',"")for i in file1.readlines()]
num=random.randrange(0,len(list1))
print(list1[num])

