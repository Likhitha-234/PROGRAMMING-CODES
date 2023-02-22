def ithoccurance(lst):
    count=0
    b=int(input("enter the occurance: "))
    c=str(input("enter the word to be removed:"))
    for i in range(0,len(lst)+1):
        if lst[i]==c:
            count+=1
            if count==b:
                del lst[i]
                break
    return lst
#lst=["hello","hi","hello","byee","likki","hello","abc","hi","yyg","hi"]
#print(ithoccurance(lst))