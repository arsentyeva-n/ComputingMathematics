import math
def funcA(x):
    return (4 * x) + (2 ** x) + 6

def funcB(x):
    return (-2 * x ** 3) - (2 * x ** 2) + (2 * x) + 5



def Function(f, a, b):
    n = 0
    c = (a + b) / 2
    E = 0.0001
    
    print ("k     a    b    (a + b) / 2")
    print (n,"  ", a, "  ", b, "  ", c)
    while (b - a) >= 2 * E:
        if f(a) * f(c) < 0: b = c
        elif f(b) * f(c) < 0 : a = c
        elif f(c) == 0 : break
        
        c = (a + b) / 2
        n = n + 1
        print (n,"  ", round(a,4), "  ", round(b,4), "  ", round(c,4))

a = -2
b = -1    
print("Метод половинного деления")
print("1 уравнение")
Function(funcA,a,b)

print("2 уравнение")
a = -2
b = -1    

Function(funcB,a,b)