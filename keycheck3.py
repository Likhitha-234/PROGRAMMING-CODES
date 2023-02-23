def checkkey(d,k):
    for i in d:
        if i==k:
            return True
d={'a':1,'b':2,'name':"likki"}
k=input("enter the key")
print(checkkey(d,k))
    
