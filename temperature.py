temperature=float(input("Enter the Temp in c: "))
if temperature<=0:
    print("cold")

elif 0<=temperature<=15:
    print("Cool")

elif 16<=temperature<=30:
    print("Warm")
    
else: print("hot")