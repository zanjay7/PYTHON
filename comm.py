x=[1,2,3,4,5]
y=[2,3,7,4,9]
temp=[]
for i in x:
    # flag=0
    for j in y:
        if i==j:
            # flag+=1
            temp.append(i)
print(temp)
            
         