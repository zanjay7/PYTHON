x=[3,3,3]
# y=x[::-1]

z1=set()
largest=0
z=[]
dif=0    
for i in range(len(x)):
    for j in range(len(x)):
        if i != j:
            dif = x[i]-x[j]
            if dif > largest:
                largest = dif
                z1.add(tuple(sorted((i, j))))
                
            # else:
            #     print("No valid pair!")
            #     break
     
    
    
print(z1)
            
