import math
x1=28.5383
y1=81.3792
short_path=0
dist=0
city=[]
lat=[]
lang=[]
dist_list=[]
dict1= {}
f1= open("location.txt" , "r")
list1=f1.readlines()
for i in range(0,len(list1),1):
    line1=list1[i].replace("\n", "")
    temp1=line1.split(":")
    city.append(temp1[0])
    latlong=temp1[1]
    temp2=latlong.split(",")
    lat.append(float(temp2[0]))
    lang.append(float(temp2[1]))
for i in range(0,len(city),1):  #taken city list length/ can taken even values 0to4
    x2=lat[i]
    y2=lang[i]
    dist=math.sqrt((math.pow(x2-x1,2)+ math.pow(y2-y1,2)))
    dist_list.append(dist)
# dist=math.sqrt(((x2 – x1)² + (y2 – y1)²))
print("Various loaction near by = ",dist_list)
short_path=min(dist_list)
index1= dist_list.index(short_path)
near_city=city[index1]
print("Shortest path = ", short_path)
print("Index Value = ",index1)
print("Nearest City to visit for testing = ", near_city)







