a=10
n1=0
n2=1
print(n1)
print(n2)
prev=0
for i in range(1,a):
    temp=n2
    n2+=prev
    print(n2)
    prev=temp