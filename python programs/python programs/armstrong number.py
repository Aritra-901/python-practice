def armstrong_number(x):
    st=str(x)
    n=len(st)
    sum=0
    for i in range(n):
        sum+=pow(int(st[i]),n)
    if x==sum:
        return"armstrong number"
    else:
        return "not armstrong number"
print(armstrong_number(1634))