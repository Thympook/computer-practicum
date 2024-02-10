import math  

x = float(input('Введите x: '))
y = float(input('Введите y: '))

q = 3 * math.cos(math.pi * x) - abs(2-y) # 3cospix - |2-y|

z = (q + ((2 + q) / (q**2 + 3))) / (1 / (math.sqrt(q**2 + 8)))

print(f'Значение z = {z}')
