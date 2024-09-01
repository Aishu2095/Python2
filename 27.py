list1=["C"]*10
print(list1)
len1=len(list1)
for i in range(0,len1,1):
    list1[i]="O"
print(list1)
for i in range(1,len1,2):
    list1[i]="C"
print(list1)
for i in range(2,len1,3):
    if list1[i]=="O":
        list1[i]="C"
    else:
        list1[i]="O"
print(list1)
for i in range(3,len1,4):
    if list1[i]=="O":
        list1[i]="C"
    else:
        list1[i]="O"
print(list1)



