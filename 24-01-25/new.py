# def revs(a):
#     return a[::-1]
def pali(s):
    str=""
    for i in s:
        str=i+str
    if s==str:
        print("Is palindrome")
        
    else:print("Not palindrome")