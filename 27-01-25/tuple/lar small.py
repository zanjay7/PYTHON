tuple1=(2,5,4,7,8,2,2,6,4,5,10)
x=list(tuple1)
largest=x[0]
smallest=x[0]
for i in x:
    if i < smallest:
        smallest = i
    elif i > largest:
        largest = i
       
print(largest,smallest)