# Задание 1

import math

def f(x):
    n = int(input())  
    a = []
    for i in range(n):
        x = int(input())  
        a.append(x)


    for i in range(len(a)):
        a1 = []
        if a[i] > 0:
            a1.append(math.log(a[i]))
        else:
            a1.append("None")
        return a1 
x1 = []
print(f(x1))



# Задание 2

a = [1, 50, 20, 50]
b = ["Володин", "Гришин", "ещё кто-то", "Просто чел"]

def f(a, b):
    if len(a) != len(b):
        print( "Списки имеют разную длину")
    else:
        us = dict()
        for i in range(len(a)):
            us.update({a[i]: b[i]})
    return us

print(f(a, b))


# Задание 3


def f(p, n, k):
    a, b, c = 1, 1, 1
    for i in range(2, n + 1):
        a = a * i
    for i in range(2, k + 1):
        b = b * i
    for i in range(2, n - k + 1):
        c = c * i
    res = (a /(b * c)) * p**k * (1 - p)**(n - k)
    return 'P(x) = ', res

print(f(0.5, 10, 5))


# Задание 4


def f(n):
    s = n.split(",")
    s.sort()
    return s

print(f("15, 10, -1"))