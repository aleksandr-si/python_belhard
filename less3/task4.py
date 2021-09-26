import math

fig=input('enter the figure type: ')

if fig=='треугольник':
    a=float(input('enter a size'))
    b=float(input('enter b size'))
    c=float(input('enter c size'))
    p=(a+b+c)/2
    print((p*(p-a)*(p-b)*(p-c))**0.5)
elif fig=='прямоугольник':
    a=float(input('enter a size'))
    b=float(input('enter b size'))
    print(a*b)
elif fig=='круг':
    a=float(input('enter r size'))
    print(math.e*(a**2))
    