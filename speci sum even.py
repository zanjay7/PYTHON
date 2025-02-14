x=[1,2,4,3,4,2,6]
# y=x[::-1]
sum=int(input("Enter the sum: "))

z=set()
# n=[]
# for i in x:
#     if i%2==0:
#         n.append(i)
        
for i in range(len(x)):
    for j in range(len(x)):
        if x[i]%2==0 and x[j]%2==0:
            if x[i]*x[j]==sum:
                z.add(tuple(sorted((i, j))))
print(z)

# y=[]
# for i in range(len(z)):
#     for i in range(len(n)):
#         if z[i]==n[j]:
#             y.append(j)