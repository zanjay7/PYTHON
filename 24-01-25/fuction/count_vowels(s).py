def count_vowels(s):
    count=0
    for i in s:
        if i in 'aeiouAEIOU':
            count=count+1
    
    print(f"{count}")

s=input("Enter the string: ")
count_vowels(s)