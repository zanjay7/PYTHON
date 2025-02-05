x = [1, 10, 3, 4, 5, 6, 7, 8, 10, 10]
temp=[]
for i in range(len(x)):
    for j in range(i,(len(x))):
        if x[i]>x[j]:
            temp=x[i]
            x[i]=x[j]
            x[j]=temp
print(temp)
    
    
        