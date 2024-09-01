x1=28.5383
y1=81.3792
city=[]
lat=[]
lang=[]
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
print(lat,lang)
print(city)
