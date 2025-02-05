num=int(input("Enter the range of array: "))
n=[]

for i in range(num):
    li=int(input("Enter the Array:"))
    n.append(li)
print(n)
product=1
for i in n:
    product*=i
print(product)
    
