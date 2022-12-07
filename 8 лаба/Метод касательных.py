import sys
import math
from prettytable import PrettyTable


def f(x):
    return 2 * math.exp(x) - 2 ** x

def df(x):
    return 2 * math.exp(x) - 2 * x
 
def ddf(x):
    return 2 * math.exp(x) - 2

# def funcA(x):
#     return (4 * x) + (2 ** x) + 6
# 
# def funcB(x):
#     return (-2 * x ** 3) - (2 * x ** 2) + (2 * x) + 5


def Function(f, a, b,table):
    n = 0

    flag = True
      
    if f(a) * ddf(a) > 0 :
        cnew = a - f(a) / df(a)
    elif f(b) * ddf(b) > 0 :
        cnew = b - f(b) / df(b)
    else :
        flag = False
        print("Вычисления невозможны")
    
    if flag == True :
        E = 0.0001
        table.add_row ([n, round(a,4), round(b,4), round(cnew,4)])
        while True:
            if f(a) * f(cnew) < 0 :
                b = cnew
            elif f(b) * f(cnew) < 0 : a = cnew
            elif f(cnew) == 0 : break
            cold = cnew
            
            if f(a) * ddf(a) > 0 :
               cnew = a - f(a) / df(a)
            elif f(b) * ddf(b) > 0 :
                cnew = b - f(b) / df(b)
            else :
                print("Вычисления невозможны")
                break
            n += 1
            table.add_row ([n, round(a,4), round(b,4), round(cnew,4)])
            if abs(cnew - cold) > E: break
print("Метод касательных")

print("1 уравнение")
a = -1
b = 0   
t1 = PrettyTable (['k', 'a', 'b', 'cnew'])
Function(f,a,b,t1)
print(t1)

# print("2 уравнение")
# a = 1
# b = 1.5    
# t2 = PrettyTable (['k', 'a', 'b', '(a + b) / 2'])
# Function(funcB,a,b,t2)
# print(t2)
