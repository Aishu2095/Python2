f1=open("convert.txt","r")
while f1:
    str1=f1.readline().replace("\n","")
    list1=str1.split(" ")
    lhs_value=float(list1[0])
    lhs_units=(list1[1])
    rhs_value=float(list1[3])
    rhs_units=list1[4]
    result1= str(1)+" "+lhs_units+" = "+str(rhs_value/lhs_value)+" "+rhs_units 
    print(result1)
    result2= str(1)+" "+rhs_units+" = "+str(lhs_value/rhs_value)+" "+lhs_units
    print(result2)
    print()
    if f1=="":
        break


