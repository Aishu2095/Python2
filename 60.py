f1=open("Passage.txt","r")
f2=open("sorted_passage.txt","w")
special=["!","@","#","$","%","^","&","*","(",")","_","+",",",".",";","?"]
line1=""
list1=[]
list3=[]
while True:
    line1=f1.readline().strip()
    list2=line1.split(" ")
    for i in list2:
        list1.append(i)
    if line1=="":
        break
list1.remove("")
set1=set(list1)
list1=list(set1)
list1.sort()
for i in list1:
    f2.write(i)
    f2.write("\n")
f2.close()
print(list1) 

