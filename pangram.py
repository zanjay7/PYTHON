x=input("enter the sentence: ")
for i in x:
    if 'abcdefghijklmnopqrstuvwxyz' in i:
        print("Pangram")
        break
    else: print("not pangram")
    break