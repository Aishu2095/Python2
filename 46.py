f1=open('marks.txt', 'r')
list1=[]
list2=[]
total_marks=[]
english_topper=[]
maths_topper=[]
physic_toppoer=[]
chemistry_topper=[]
biology_topprt=[]
names=[]
e_marks=[]
m_marks=[]
p_marks=[]
c_marks=[]
b_marks=[]
pos=0
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
maths_max=max(m_marks)
physic_max=max(p_marks)
chemistry_max=max(c_marks)
biology_max=max(b_marks)

for i in range(0, len(names)):
    if e_marks[i]==english_max:
        print("Name of English top Scorer: ", names[i])
    #print()
    if m_marks[i]==maths_max:
        print("Name of Maths top scorer: ", names[i])
    #print()
    if p_marks[i]==physic_max:
        print("Name of Physic top Scorer: ", names[i])
    #print()
    if c_marks[i]==chemistry_max:
        print("Name of Chemistry top Scorer: ", names[i])
    #print()
    if b_marks[i]==biology_max:
        print("Name of Biology top Scorer: ", names[i])
    #print()
    total1=e_marks[i]+m_marks[i]+p_marks[i]+c_marks[i]+b_marks[i]
    total_marks.append(total1)

# we have e_marks just to have or know a length of students 
print()   
max1=max(total_marks)
pos=total_marks.index(max1)
goldmedalist=names[pos]
print("The Gold Medalist is:", goldmedalist)



