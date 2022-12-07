import sys
from prettytable import PrettyTable


def funcA(x):
    return (4 * x) + (2 ** x) + 6

def funcB(x):
    return (-2 * x ** 3) - (2 * x ** 2) + (2 * x) + 5


def Function(f, a, b,table):
    n = 0
    c = (a + b) / 2
    E = 0.0001
    
    table.add_row ([n, round(a,4), round(b,4), round(c,4)])

    while (b - a) >= 2 * E:
        if f(a) * f(c) < 0: b = c
        elif f(b) * f(c) < 0 : a = c
        elif f(c) == 0 : break
        
        c = (a + b) / 2
        n = n + 1
        table.add_row ([n, round(a,4), round(b,4), round(c,4)])
        
print("Метод половинного деления")

print("1 уравнение")
a = -2
b = -1   
t1 = PrettyTable (['k', 'a', 'b', '(a + b) / 2'])
Function(funcA,a,b,t1)
print(t1)

print("2 уравнение")
a = 1
b = 1.5    
t2 = PrettyTable (['k', 'a', 'b', '(a + b) / 2'])
Function(funcB,a,b,t2)
print(t2)