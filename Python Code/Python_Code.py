n = int(input())
matrix1 = []
matrix2 = []
final = []
for i in range(n):
    m1 = []
    x = input().split(',')
    for j in x:
        m1.append(int(j))
    matrix1.append(m1)
for k in range(n):
    m2 = []
    x = input().split(',')
    for l in x:
        m2.append(int(l))
    matrix2.append(m2)
for i in range(n):
    x = []
    for j in range(n):
        x.append(matrix1[i][j]+matrix2[i][j])
    final.append(x)
for i in range(n):
    for j in range(n):
        if(j!=n-1):
            print(final[i][j], end=",")
        else:
            print(final[i][j])



    


