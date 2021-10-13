'''
Реализовать генератор, который будет выводить числа фибоначчи.
'''

print(0)
print(1)
def gen_fib(a):
    a=a
    x1=0
    x2=1
    x3=0
    for i in range(1,a+1):
        x3=x2
        x2=x1+x2
        x1=x3
        print(x2)
    yield(x2)

val=gen_fib(200)
val
next(val)
print((val))

