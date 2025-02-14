tuple1=("apple","banana","mango","pappaya","cherry")
# x=list(tuple1)

# for i in range(len(x)):
#     for j in range (i,len(x)):
#         temp=x[i]
#         x[i]=x[j]
#         x[j]=temp
        
# print(x)
b=(tuple1[-1],)+tuple1[1:-1]+(tuple1[0],)
print(b)

