list=[5,10,15,20,10]
n=int(input("enter:"))
temp=[]
for i in list:
    if i % n !=0:
        temp.append(i)
print(temp)
        