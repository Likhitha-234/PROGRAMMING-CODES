def sum(n):
    if n<0:
        return "cant add negative numbers"
    if n==0:
        return 0
    sum=0
    while(n!=0):
        sum=sum+(n%10)
        n=n//10
    return sum
print(sum(-4))




