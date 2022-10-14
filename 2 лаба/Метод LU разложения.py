# A = [[8,-3,7,-7,8,-9,-7],
#      [2,-8,0,0,-1,-6,6],
#      [1,-2,-7,2,8,3,0],
#      [9,-6,-4,3,-8,8,-4],
#      [0,-4,2,-3,-6,-3,1],
#      [-3,9,1,0,7,-5,-8]]

A = [[-0.74,0.47,-0.15,-0.3,0.81,-0.97],
     [0.01,-0.65,-0.64,0.58,-0.04,-0.86],
     [-0.33,0.01,-0.61,-0.95,0.19,-0.82],
     [-0.96,-0.42,-0.03,0.68,-0.71,0.99],
     [0.07,0.73,-0.97,0.84,-0.35,-0.11]]


n = len(A)
B = [0] * n
T = [0] * n
X = [0] * n
Y = [0] * n
C = [0] * n

for i in range(n):
    C[i] = A[i][n]
    B[i] = [0] * n
    T[i] = [0] * n
    for j in range(n):
        if i == j : T[i][j] = 1;
    
#Заполнение крайнего столбца матрицы В
for i in range(n):
    B[i][0] = A[i][0]

#Заполнение верхней строки матрицы T
for j in range(1,n):
    T[0][j] = A[0][j]/B[0][0]

#Заполнение матриц B и T
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
#Вывод
print('Матрица Т:')
for i in range(n):
    for j in range(n):
        print("{:4.3f}".format(T[i][j]), end=' ')
    print(' ')
print(' ')

#Вывод
print('Матрица В:')
for i in range(n):
    for j in range(n):
        print("{:4.3f}".format(B[i][j]), end=' ')
    print(' ')
print(' ')

#Вычисление вектора Y
Y[0] = C[0] / B[0][0]
for i in range(1,n):
    Y[i] = C[i]
    for m in range(i):
        Y[i] = Y[i] - B[i][m] * Y[m]
    Y[i] = Y[i] / B[i][i]

print('Вектор Y:')
for i in range(n):
    print("{:0.3f}".format(Y[i]), end=' ')

#Вычисление вектора X
X[n-1] = Y[n-1]
for i in range(n-2, -1, -1):
    X[i] = Y[i]
    for m in range(i+1,n):
        X[i] = X[i] - T[i][m] * X[m]

print('\nВектор X:')
for i in range(n):
    print("{:0.3f}".format(X[i]), end=' ')