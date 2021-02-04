def prime_number(x):
    if x>1:
        for i in range(2,x):
            if(x%1==0):
                return "it is prime"
            else:
                return "not prime"
print(prime_number(9))            