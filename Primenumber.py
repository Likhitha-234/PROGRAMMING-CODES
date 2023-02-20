

def prime(n):
    for i in range(2,n):
        if(n%i)==0:
            return "yes it is not prime"
        else:
            return "yes it is prime"
        
