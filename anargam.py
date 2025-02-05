str=input("Enter the string:")
str2=input("enter the second string:")
flag=0
len1=len(str)
len2=len(str2)
if len1==len2:
    for i in str:
        if i in str2:
            flag=1

    
    
if flag!=0:
    print("Anagram")
else:print("Not anagram")


        