n=int(input("Enter the No: "))
count=0
for i in range (2 ,n):
    
    if n%i==0:
        count=+1
        
if count==0:
    print("prime") 
    
else:print("NOT PRIME")    
    
