f1=open('marks.txt', 'r')
list1=[]
list2=[]
names=[]
e_marks=[]
m_marks=[]
p_marks=[]
c_marks=[]
b_marks=[]
while f1:
    line1=f1.readline().replace('\n', "")
    list1.append(line1)
    if line1=="":
        break
list1.remove('')
'''print(list1)'''
for i in list1:
    list2=i.split(',')
    names.append(list2[0])
    temp=list2[3].split(':') #list2[3] contains english: marks 
    e_marks.append(int(temp[1]))
    '''temp has two values i.e english and marks hence [1]= marks'''
    temp=list2[4].split(':')#list2[4] contains maths: marks
    m_marks.append(int(temp[1]))
    temp=list2[5].split(':')
    p_marks.append(int(temp[1])) # int is added coz string is converted into int without int it will pass string value
    temp=list2[6].split(':')
    c_marks.append(int(temp[1])) # if no int then it will take ASCI value
    temp=list2[7].split(':')
    b_marks.append(int(temp[1]))
    
english_max= max(e_marks)
print(english_max)
maths_max=max(m_marks)
print(maths_max)
physic_max=max(p_marks)
print(physic_max)
chemistry_max=max(c_marks)
print(chemistry_max)
biology_max=max(b_marks)
print(biology_max)


