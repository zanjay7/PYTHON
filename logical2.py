x=[]
num=int(input("Enter the range of the list:"))
for i in range(num):
    li=int(input("Enter the list:"))
    x.append(li)
    
print(x)
y=[]

a=max(x)
for i in range(1,a):
    y.append(i)
    
# print(y)
z=set()
for i in x:
    for j in y:
        if j not in x:
            z.add(j)
print(z)
            
