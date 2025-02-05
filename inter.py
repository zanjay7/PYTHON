num=int(input("Enter the range of array: "))
n=[]


for i in range(num):
    li=int(input("Enter the Array:"))
    n.append(li)
print(n)
num1=int(input("Enter the range of array: "))
n1=[]
for i in range(num1):
    liw=int(input("Enter the Array:"))
    n1.append(liw)
print(n1)
temp=[]

for i in n:
    for j in n1:
        if i==j:
            if i not in temp:
                temp.append(i)

print(temp)