num = int(input("Enter the Nth Number: "))

for i in range(num):
    x = i + 1
    if x % 2 == 0:
        print(x)
