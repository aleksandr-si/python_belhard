import math
first_val=0
secon_val=0
while math.trunc(first_val) not in range(3,23):
    first_val=float(input('enter first var 3-23: '))

while math.trunc(secon_val) not in range(3,23):
    secon_val=float(input('enter seca var 3-23: '))

oper_val=input('enter operation: ')

if oper_val=='+':
    print(first_val+secon_val)
elif oper_val=='-':
    print(first_val-secon_val)
elif oper_val=='*':
    print(first_val*secon_val)
elif oper_val=='/':
    print(first_val/secon_val)
elif oper_val=='%':
    print(first_val%secon_val)
