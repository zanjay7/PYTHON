x = [1, 99999, 3, 4, 5, 6, 100, 8, 10, 10]
temp=[]
for i in range(len(x)):
    for j in range(i,(len(x))):
        if x[i]>x[j]:
            temp=x[i]
            x[i]=x[j]
            x[j]=temp
small=[]
for i in range(len(x)):
    for j in range(i,(len(x))):
        if x[i]<x[j]:
            small=x[i]
            x[i]=x[j]
            x[j]=small
print(small)  
print(temp)
print(x)