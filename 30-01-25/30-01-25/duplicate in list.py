x = [1, 2, 2, 3, 4, 4, 5]
temp = []

for i in x:
    if i not in temp:
        temp.append(i)
print(temp)