def vowels(s):
    L=[]
    for i in "aeiouAEIOU":
        if i in s:
            L.append(i)
    return L
print(vowels("likki"))