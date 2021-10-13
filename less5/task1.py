'''
Задача 1.
Реализовать класс комплексное число.
Реализовать 4 базовые операции:
+, -, /, *
Добавить подсчет модуля числа.
'''
class Complex:
 
    def __init__(self, x, y):
        self.rez = x
        self.im = y
 
    def repr(self):
        return f'Complex: {self.rez} + ({self.im})i'
 
class Complex:
 
    def __init__(self, x, y):
        self.rez = x
        self.im = y
 
    def __repr__(self):
        return f'Complex: {self.rez} + ({self.im})i'
 
    def __add__(self, right):
        if isinstance(right, int):
            return Complex(self.rez + right, self.im)
        if isinstance(right, Complex):
            return Complex(self.rez + right.rez, self.im + right.im)
 
    def __eq__(self, right):
        if isinstance(right, Complex):
            return (right.rez == self.rez) and (right.im == self.im)
 
    def __abs__(self):
        return (self.rez ** 2 + self.im ** 2) ** 0.5

    def __mul__(self, right):
        a=self.rez*right.rez-(self.im*right.im)
        b=self.rez*right.im+self.im*right.rez
        if b<0:
            return (f"{a}{b}i")
        else:
            return (f"{a}+{b}i")
    def __truediv__(self, right):
        x = self.rez * right.rez + self.im * right.im
        y = self.im * right.rez - self.rez * right.im
        z = right.rez**2 + right.im**2
        rez = x / z
        im = y / z
        return Complex(rez, im)
        
a = Complex(2, -5)
b = Complex(1, -5)
print(a+b)
print(a == b)
print(abs(a))
print(a*b)
print(a/b)