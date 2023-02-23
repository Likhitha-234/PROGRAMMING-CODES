def naturalsum(n):
    if n==0:
        return 0
    return naturalsum(n-1)+n
print(naturalsum(10))
