start=7
end =27
for i in range(start,end):
    if i>1:
        for j in range(2,i):
            if(i%j==0):
                break
        else:
             print(i)
