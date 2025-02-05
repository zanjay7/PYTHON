tuple1=("apple","banana","mango","pappaya","cherry")
x=list(tuple1)

for i in range(len(x)):
    for j in range (i,len(x)):
        temp=x[i]
        x[i]=x[j]
        x[j]=temp
tuple2=tuple(x)
print(tuple2)