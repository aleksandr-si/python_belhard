# class Complex:
#     def __init__(self,x,y):
#         self.rez=x
#         self.im=y
#     def __repr__(self) -> str:
#         return f'Complex: {self.rez}+({self.im})i'
#     def __add__(self,right):
#         if isinstance (right,int):
#             return Complex(self.rez + right, self.im)
#         if isinstance(right,Complex):
#             return Complex(self.rez+right.rez,self.im+right.im)
#     def __eq__(self, right) -> bool:
#         if isinstance(right,Complex):
#             return

# a=Complex(1,5)
# print(a)

class Point:

    def __init__(self,*args) -> None:
        self.choords=args
    def __abs__(self):
        return sum([x**2 for x in self.choords]) ** 0.5
    