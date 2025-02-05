x=[2,4,3,7,5,8,1]
y=x[::-1]
sum=int(input("Enter the sum: "))

z=set()
for i in x:
    for j in x:
        if i!=j:
            if i+j==sum:
                z.add(tuple(sorted((i, j))))
                
print(list(z))