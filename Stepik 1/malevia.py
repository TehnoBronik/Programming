from math import sqrt
sh = (input())
if sh == "треугольник":
    a = (int(input()))
    b = (int(input()))
    c = (int(input()))
    p = ( a + b + c ) / 2
    s = sqrt(p*(p-a)*(p-b)*(p-c))
    print(s)
elif sh == "прямоугольник":
    a = (int(input()))
    b = (int(input()))
    s = a * b
    print(s)
elif sh == "круг":
    r = (int(input()))
    s = 3.14 * r * r
    print(s)
