
def prime(a):
    s ="not prime"
    if a>1:
        for i in range(2,a):
           
            if(a%i)==0:
             
               s="not prime"
            
               break
        
            else:
             
                s="prime"
             
    else:
                 
        s = "not prime"
                 
    return(s)
            
print(prime(3))