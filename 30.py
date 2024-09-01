count=100
lucky=[]
unlucky=[]
list1=["C"]*count
print(list1)
len1=len(list1)
for i in range(0,len1,1):
    list1[i]="O"
print(list1)
for i in range(1,len1,2):
    list1[i]="C"
print(list1)

for j in range(2,count,1):
    for i in range(j,len1,j+1):
        if list1[i]=="O":
            list1[i]="C"
        else:
            list1[i]="O"
    print(list1)
for i in range(0,len1,1):
    if list1[i]=="O":
        lucky.append(i+1)
    else:
        unlucky.append(i+1)
print(lucky,"Are the lucky prisoners, who are going to be resleased today")
print(unlucky,"Unlucky prisoners who will be released after 4 weeks")



