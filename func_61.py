def function1(fname):
    f1=open(fname,"r")
    list1=[]
    special=["!","@","#","$","%","^","&","*","(",")","_","+",",",".",";","?"]
    while True:
        line1=f1.readline().strip()
        for i in special:
            line1=line1.replace(i,"")
        list1.append(line1)
        if line1=="":
            break
    list1.remove("")
    return list1
