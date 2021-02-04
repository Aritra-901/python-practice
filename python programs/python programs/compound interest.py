def compound_interest(p,r,t):
    a=p*pow((1+(r/100)),t)
    ci=a-p
    return ci
print(compound_interest(1000,10.25,5))