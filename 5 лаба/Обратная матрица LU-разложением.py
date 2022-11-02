n = 4

# A = [[8,1,2,1,4,9],
#      [9,7,7,3,4,3],
#      [4,3,9,7,2,9],
#      [5,4,7,3,8,4],
#      [3,6,4,4,5,3],
#      [9,2,8,3,6,9]]

A = [[-1,-1,-1,-2],
     [2, 3, 4, 3],
     [-2, 0, 1,-6],
     [-2,-2,-3,-3]]

B = [0] * n
T = [0] * n 
Y = [0] * n
X = [0] * n
O = [0] * n

# Первичное заполнение матриц B, T
for i in range(n):
    B[i] = [0] * n
    T[i] = [0] * n
    Y[i] = [0] * n
    X[i] = [0] * n
    O[i] = [0] * n
    for j in range(n):
        if i==j : T[i][j] = 1
        
#Вычисление матриц B и T
for i in range(n):
    B[i][0] = A[i][0]

for j in range(1,n):
    T[0][j] = A[0][j] / B[0][0]

for k in range(1,n):
    for i in range(k,n):
        B[i][k] = A[i][k]
        for m in range(k):
            B[i][k] = B[i][k] - B[i][m] * T[m][k]
    if k <= n - 2 :
        for j in range(k+1,n):
            T[k][j] = A[k][j]
            for m in range(k):
                T[k][j] = T[k][j] - B[k][m] * T[m][j]
            T[k][j] = T[k][j] / B[k][k]

#Вывод матриц B и T
print('Матрица B:')
for i in range(n):
    for j in range(n):
        print("{:4.3f}".format(B[i][j]), end=' ')
    print(' ')
print(' ')

print('Матрица Т:')
for i in range(n):
    for j in range(n):
        print("{:4.3f}".format(T[i][j]), end=' ')
    print(' ')
print(' ')

#Вычисление и вывод матрицы Y
for i in range(n):
    for j in range(n):
        if j > i :
            Y[i][j] = 0
        elif j == i :
            Y[i][j] = 1 / B[i][i]
        elif j < i :
            Y[i][j] = 0
            for m in range(j,i):
                Y[i][j] = Y[i][j] - B[i][m] * Y[m][j]
            Y[i][j] = Y[i][j] / B[i][i]
            
print('Матрица Y:')
for i in range(n):
    for j in range(n):
        print("{:4.3f}".format(Y[i][j]), end=' ')
    print(' ')
print(' ')

#Вычисление и вывод матрицы X
for i in range(n-1,-1,-1):
    for j in range(n-1,-1,-1):
        if j < i :
            X[i][j] = 0
        elif j == i :
            X[i][j] = 1
        elif j > i :
            X[i][j] = 0
            for m in range(i+1,j+1):
                X[i][j] = X[i][j] - T[i][m] * X[m][j]
                
print('Матрица X:')
for i in range(n):
    for j in range(n):
        print("{:4.3f}".format(X[i][j]), end=' ')
    print(' ')
print(' ')


#Вычисление и вывод матрицы, обратной к A
for i in range(n):
    for j in range(n):
        O[i][j] = 0
        for m in range(n):
            O[i][j] = O[i][j] + X[i][m] * Y[m][j]
            
print('Обратная к матрице A:')
for i in range(n):
    for j in range(n):
        print("{:6.0f}".format(O[i][j]), end=' ')
    print(' ')
print(' ')