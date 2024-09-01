import random
umarks=[]
cmarks=[]
temp=[]
lastchar1=""
lastchar2=""
file1=open("dictionary.txt","r")
list1=[i.replace('\n',"")for i in file1.readlines()]
num=random.randrange(0,len(list1))
computerchoise=(list1[num])
print("Computer: ",computerchoise)
len1=len(computerchoise)
cmarks.append(len1)
lastchar1=computerchoise[-1]
'''this is called string slicing -1 takes last character,
in case if we have to take first character the (0,1)'''
print(lastchar1)
while True:
    userchoise=input("User: ")
    if userchoise in list1 and userchoise.startswith(lastchar1):
        len1=len(userchoise)
        umarks.append(len1)
        lastchar2=userchoise[-1]
        temp=filter(lambda j: j.startswith(lastchar2),list1)
        temp=list(temp)
        num=random.randrange(0,len(temp))
        computerchoise=temp[num]
        print("Computer: ", computerchoise)
        len1=len(computerchoise)
        cmarks.append(len1)
        lastchar1=computerchoise[-1]
        print(lastchar1)
        list1.remove(computerchoise)
        list1.remove(userchoise)
    else:
        print("The word is not correct or the word is repeated")
        break
print("User Marks is: ", sum(umarks))
print("Computer Marks is: ", sum(cmarks))

    



        
'''lambda is used to write many line code into one line code, j was defined character like i
condition given for user and system input'''

