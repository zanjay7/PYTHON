def remove_duplicates(lst):
    set1 = set()
    lst1 = []
    
    for i in lst:
        if i not in set1:
            set1.add(i)
            lst1.append(i)
    
    print(lst1)

lst = [1, 2, 2, 3, 4, 4, 5, 1]
remove_duplicates(lst)
