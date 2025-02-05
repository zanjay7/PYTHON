x={1, 2, 3, 4} 
y={3, 4, 5, 6,10}
diff=set()
for i in x:
    for j in y:
        if i not in y:
            diff.add(i)
            # diff.add(j)
        if j not in x:
            diff.add(j)
print(diff)

