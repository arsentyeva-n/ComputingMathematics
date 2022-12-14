# A = [[75,-3,7,-7,8,-9],
#     [2,20,0,0,-1,-6],
#     [1,-2,22,2,8,3],
#     [9,-6,-4,101,-8,8],
#     [0,-4,2,-3,35,-3],
#     [-3,9,1,0,7,25]]
# 
# B = [-7, 6, 0, -4, 1, -8]

A = [[25,4,7,-3,-1],
     [-8,42,8,-9,-3],
     [-6,4,34,4,-8],
     [-8,4,7,36,9],
     [6,-6,-2,-4,29]]

B = [32, 60, 84, 96, 23]

n = len(A)
X = [0] * n
X2 = [0] * n
k = 0
E = 0.001

# # Проверка, что сумма всех модулей элементов в i строке кроме элемента по диагонали меньше модуля элемента по диагонали 
# for i in range(n):
#     if sum(abs(A[i])) > 2 * abs(A[i][i]) : exit(); #не работает

while True:
    k = 0
    for i in range(n):
        X[i] = B[i]
        # Нахождение значения X[i]
        for j in range(n):
            X[i] = X[i] - A[i][j] * X2[j]
        X[i] = (X[i]  + A[i][i] * X2[i]) / A[i][i] 
    # Вывод значений
    for i in range(n):
        print("{:0.4f}".format(X[i]), end=' ')
    print()
    # Цикл работает, пока все переменные не достигнут точности E
    for i in range(n):
        if abs(X[n-1] - X2[n-1]) < E : k+=1;
    if k == n: break;
    # Сохранение X[i] для нового вычисления
    for j in range(n):
        X2[j] = X[j]
