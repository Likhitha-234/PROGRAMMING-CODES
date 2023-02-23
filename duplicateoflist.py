def duplicate(lst):
    lst1=[]
    for i in lst:
        if i not in lst1:
            lst1.append(i)
    return lst1
lst=[1,2,3,1,4,51,1,2,76,51]
print(duplicate(lst))
