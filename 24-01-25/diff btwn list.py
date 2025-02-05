list1=[1,2,3,4]
list2=[3,4,5,6,7,8,1]
li=[]
for i in list1:
    if i not in list2:
        li.append(i)
print(li)
    
            