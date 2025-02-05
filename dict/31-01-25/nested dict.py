nested_dict={}
datas1=int(input("Enter the No of datas in the dict: "))

for i in range(datas1):
    outer_key=input("Enetr the Outer Keys: ")
    
    datas2=int(input("Enter the No of datas in inner dict: "))
    
    nested_dict[outer_key]={}
    
    for i in range(datas2):
    
        inner_key=input("Enetr the inner Keys: ")
    
        values_inner=input("Enter the inner values: ")
        nested_dict[outer_key][inner_key]=values_inner
print(nested_dict)
    