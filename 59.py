def data1():
    num1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,30,40,50,60,70,80,90,100]
    words1 = ['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty','thirty','forty','fifty','sixty','seventy','eighty','ninty','hundred']
    return [num1,words1]

def method1(input1):
    num1=data1()[0]
    words1=data1()[1]
    for i in range(0, len(num1),1):
        if input1 == num1[i]:
            pos=i
    result1=words1[pos]
    return result1
    
def method2(input1):
    num1=data1()[0]
    words1=data1()[1]
    part1=(input1//10)*10
    part2=input1%part1
    fullword= method1(part1)+' '+method1(part2)
    return fullword

print('Type 0 to Stop')
while True:
    input1=int(input('Enter a number: '))
    if input1>0:
        num1=data1()[0]
        if input1 in num1:
            print(method1(input1))
        elif input1>=21 and input1<=100:
            print(method2(input1))
    else:
        break



    
