def is_prime(n):
    count=0
    for i in range (2 ,n):
        
        if n%i==0:
            count=+1
            
    if count==0:
        print("prime") 
        
    else:print("NOT PRIME") 
n=int(input("Enter the No: "))
is_prime(n)
