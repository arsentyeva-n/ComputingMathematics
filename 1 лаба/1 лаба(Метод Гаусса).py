matrix = [[-0.74,0.47,-0.15,-0.3,0.81,-0.97],
         [0.01,-0.65,-0.64,0.58,-0.04,-0.86],
         [-0.33,0.01,-0.61,-0.95,0.19,-0.82],
         [-0.96,-0.42,-0.03,0.68,-0.71,0.99],
         [0.07,0.73,-0.97,0.84,-0.35,-0.11]]

n = len(matrix)
x = [0] * n

#основной цикл
for k in range(n):
    #Проверка, что matrix[k][k] != 0
    if abs( matrix[k][k] ) < 0.00001 :
        m = k + 1
        while abs( matrix[m][k] ) < 0.00001 :
            m = m + 1
        #Перемена местами строк k и m
        for j in range(n+1):
            temp = matrix[k][j]
            matrix[k][j] = matrix[m][j]
            matrix[m][j] = temp
            
    #Применение правила треугольника    
    for i in range(k+1,n):
        for j in range(k+1,n+1):
            if i != k : matrix[i][j] = ( matrix[i][j] * matrix[k][k] - matrix[k][j] * matrix[i][k] ) / matrix[k][k]
    #Обнуление элементов k-столбца
    for i in range(k+1,n):
        if i != k : matrix[i][k] = 0
    #деление k-й строки на matrix[k][k]
    for j in reversed(range(n+1)):
        matrix[k][j] = matrix[k][j] / matrix[k][k]
    for i in range(n):
        for j in range(n+1):
            print ( "{:4.3f}".format(matrix[i][j]),  end = " " )
        print()
    print()

#Обратный ход
for k in reversed(range(n)):
    if k == n - 1 : x[k] = matrix[k][k+1]
    else :
        x[k] = matrix[k][n]
        for j in range(n-1,k,-1):
            x[k] = x[k] - x[j] * matrix[k][j]
            
#Вывод решения        
for i in range(n):
    print("x", i+1, "= {:0.3f}".format(x[i]))