x={2, 4, 6}
y={1, 2, 3, 4}
z=set()
for i in x:
    for j in y:
        if i==j:
            z.add(i)
print(z)