from math import sqrt

figure = input()

if figure == "треугольник":
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    S = sqrt(p * (p - a) * (p - b) * (p - c))
    print (S)
elif figure == "круг":
    r = int(input())
    S = 3.14 * r ** 2
    print (S)
elif figure == "прямоугольник":
    a = int(input())
    b = int(input())
    S = a * b
    print (S)