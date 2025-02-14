x = input("Enter the string: ")

y = {}  


for i in x:
    if i in y:
        y[i] += 1
    else:
        y[i] = 1
        
freq=list(y.values())

first_value=freq[0]

count=False
for i in y:
    if i!=first_value:
        count=True
        break
print(count)


