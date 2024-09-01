import random
temp=[]
lastchar1=""
lastchar2=""
file1=open("dictionary.txt","r")
list1=[i.replace('\n',"")for i in file1.readlines()]
num=random.randrange(0,len(list1))
computerchoise=(list1[num])
print("Computer: ",computerchoise)
lastchar1=computerchoise[-1]
'''this is called string slicing -1 takes last character,
in case if we have to take first character the (0,1)'''
print(lastchar1)
while True:
    userchoise=input("User: ")
    if userchoise in list1 and userchoise.startswith(lastchar1):
        lastchar2=userchoise[-1]
        temp=filter(lambda j: j.startswith(lastchar2),list1)
        temp=list(temp)
        print(temp)
    
