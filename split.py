n=int(input("Enter the lenght of the list:"))
list=[]
for i in range(n):
    li=input("ENter the elements in the list:")
    list.append(li)
print(list)
x=n//2
print(list[:x])
print(list[x:])

