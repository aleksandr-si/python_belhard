import math

sec_int = int(input('Enter the count of seconds: '))
h = math.trunc(sec_int/3600)
m = math.trunc((sec_int-h*3600)/60)
s = sec_int-h*3600-m*60

print(f'{h} {m} {s}')