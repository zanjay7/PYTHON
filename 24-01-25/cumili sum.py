num=int(input("Enter the range:"))
list=[]
sum=[]
temp=0
for i in range(num):
    li=int(input("ENter the Elements: "))
    list.append(li)
    
for i in list:
    temp=temp+i
    sum.append(temp)
    
print(sum)