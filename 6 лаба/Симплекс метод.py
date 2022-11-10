system = [[2,5],
          [8,3]] #Коэффициенты, которые x1>=0,...,xn>=0, 

ogr = [10,24] #ограничения
f = [5,7] #Коэфф. в функции

n = len(system)
m = 2
ocn = [0]*(n+m+1)
matrix = [['Б','Сб', 1]]

for i in range(n):
    matrix = 
#основной цикл
while True:
    #Проверка, что matrix[k][k] != 0
    if abs( matrix[k][k] ) < 0.00001 : 
        m = k + 1
        while abs( matrix[m][k] ) < 0.00001 :
            m = m + 1
        #Перемена местами строк k и m
        for j in range(n):
            temp = matrix[k][j]
            matrix[k][j] = matrix[m][j]
            matrix[m][j] = temp
            
    #Применение правила треугольника    
    for i in range(n):
        for j in range(k+1,n+1):
            if i != k : matrix[i][j] = ( matrix[i][j] * matrix[k][k] - matrix[k][j] * matrix[i][k] ) / matrix[k][k]
    #Обнуление элементов k-столбца
    for i in range(n):
        if i != k : matrix[i][k] = 0
    #деление k-й строки на matrix[k][k]
    for j in reversed(range(n+1)):
        matrix[k][j] = matrix[k][j] / matrix[k][k]
    for i in range(n):
        for j in range(n+1):
            print ( "{:4.3f}".format(matrix[i][j]),  end = " " )
        print()
    print()

for i in range(n):
    print("x", i+1, "= {:0.3f}".format(matrix[i][n]))