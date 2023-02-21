# Python Program to Swap the First and Last Element in a List

def swap_firstandlast(list1):

    

    temp = list1[0]
    list1[0] = list1[-1]
    list1[-1] = temp

    return list1

list1 = [2,3,4,5,6,7,8]
print(swap_firstandlast(list1))
