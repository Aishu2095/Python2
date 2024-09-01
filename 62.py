from func_61 import function1
f2=open("sorted_passage2.txt","w")
special=["!","@","#","$","%","^","&","*","(",")","_","+",",",".",";","?"]

list1=function1("Passage.txt")
list3=[]
for i in list1:
    arr1=i.split(" ")
    for i in arr1:
        list3.append(i)
set1=set(list3)
list3=list(set1)
list3.sort()
for i in list3:
    f2.write(i)
    f2.write("\n")
f2.close()
print(list3) 

