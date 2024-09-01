f1= open('list1.txt', 'r')
f2= open('Template.txt', 'r')
f3= open('output.txt', 'w')
list2=[]
temp=[]
names=[]
amount=[]
date=[]
salutation=[]
list1= f1.readlines()
for i in list1:
    line1= i.replace('\n', '')
    temp=line1.split(',')
    if temp[0]== 'M':
        salutation.append('Mr.')
    else:
        salutation.append('Ms.')
    names.append(temp[1])
    amount.append(temp[2])
    date.append(temp[3])

template1= f2.readline().replace('\n', '')
for i in range(0,len(names),1):
    template2=template1.replace('$1salutation',salutation[i]).replace('$2name',names[i]).replace('$3amount',amount[i]).replace('$4date', date[i])              
    f3.write(template2)
    f3.write('\n')
    print(template2)
f3.close()

