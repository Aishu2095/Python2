x1=28.5383
y1=81.3792
city=[]
f1= open("location.txt" , "r")
list1=f1.readlines()
for i in range(0,len(list1),1):
    line1=list1[i]
    temp=line1.split(":")
    city.append(temp[0])
print(city)
