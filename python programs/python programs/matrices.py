x1=[[1,1,1],
    [1,1,1],
    [1,1,1]]
x2=[[1,2,3],
    [4,5,6],
    [7,8,9]]
sum=[[0,0,0],
     [0,0,0],
     [0,0,0]]
for i in range(len(x1)):
     for j in range(len(x1[0])):
          sum[i][j]=x1[i][j]+x2[i][j]
for r in sum:
     print(r)