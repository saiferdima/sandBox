f = str(input())
if f == "треугольник":
    a=float(input())
    b=float(input())
    c=float(input())
    p= ((a+b+c)/2)
    s = (((p*(p-a)*(p-b)*(p-c)))**0.5)
    print(s)
if f == "прямоугольник":
    a=float(input())
    b=float(input())
    print(a*b)
if f == "круг":
    r=float(input())
    print(r*r*3.14)
