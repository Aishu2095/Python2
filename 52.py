import math
x1=28.5383
y1=81.3792
dist=0
city=[]
lat=[]
lang=[]
dist_list=[]
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

x2=lat[0]
y2=lang[0]
# dist=math.sqrt(((x2 – x1)² + (y2 – y1)²))
dist=math.sqrt((math.pow(x2-x1,2)+ math.pow(y2-y1,2)))
dist_list.append(dist)

x2=lat[1]
y2=lang[1]
dist=math.sqrt((math.pow(x2-x1,2)+math.pow(y2-y1,2)))
dist_list.append(dist)

x2=lat[2]
y2=lang[2]
dist=math.sqrt((math.pow(x2-x1,2)+math.pow(y2-y1,2)))
dist_list.append(dist)

print(dist_list)







