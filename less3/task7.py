a=int(input('how much money on your deposit?'))
years=int(input('how long ago have you opend the deposit?'))

for i in range(1,years+1):
    a=a*0.1+a

print(a)
