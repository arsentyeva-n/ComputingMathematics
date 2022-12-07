import sys
import math
from prettytable import PrettyTable


# def f(x):
#     return 2 * math.exp(x) - 2 ** x
# 
# def df(x):
#     return 2 * math.exp(x) - 2 * x
#  
# def ddf(x):
#     return 2 * math.exp(x) - 2


def f2(x):
    return (4 * x) + (2 ** x) + 6

def df2(x):
    return math.log(2) + (2 ** x) + 4

def ddf2(x):
    return math.log(2) ** 2 + (2 ** x) 


def f1(x):
    return (-2 * x ** 3) - (2 * x ** 2) + (2 * x) + 5

def df1(x):
    return (-6 * x ** 2) - (4 * x) + 2 

def ddf1(x):
    return (-12 * x - 4)


def Function(f, df, ddf, a, b,table):
    n = 0
    c1 = 0
    c2 = 0
    flag = True
      
    if f(a) * ddf(a) > 0 :
        c1 = a
    elif f(b) * ddf(b) > 0 :
        c1 = b
        
    E = 0.0001
    while flag:
        if f(a) * ddf(a) > 0 :
            c2 = a - f(a) / df(a)
            a = c2
        elif f(b) * ddf(b) > 0 :
            c2 = b - f(b) / df(b)
            b = c2
            
        if abs(c1-c2) < E : flag = False
        
        table.add_row ([n, round(a,4), round(b,4), round(c2,4)])
        c1 = c2
        n += 1
        
        
print("Метод касательных")

print("1 уравнение")
a = 1
b = 1.5  
t1 = PrettyTable (['k', 'a', 'b', 'cnew'])
Function(f1,df1,ddf1,a,b,t1)
print(t1)

print("2 уравнение")
a = -2
b = -1    
t2 = PrettyTable (['k', 'a', 'b', 'cnew'])
Function(f2,df2,ddf2,a,b,t2)
print(t2)

# print("3 уравнение")
# a = -1
# b = 0    
# t3 = PrettyTable (['k', 'a', 'b', 'cnew'])
# Function(f,df,ddf,a,b,t3)
# print(t3)