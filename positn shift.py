n=int(input("Enter the range:"))
x=[]

for i in range(n):
    li=input("ENter the elements: ")
    x.append(li)
for i in range(len(x)-(n-1)):
    for j in range (i,n):
        temp=x[i]
        x[i]=x[j]
        x[j]=temp
        
print(x)
    