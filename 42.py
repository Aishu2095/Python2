f1=open('marks.txt', 'r')
list1=[]
while f1:
    line1=f1.readline().replace('\n', "")
    list1.append(line1)
    if line1=="":
        break
print(list1)

