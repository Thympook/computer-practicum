# Даны натуральные числа а и b, обозначающие соответственно числитель и знаменатель
# дроби. Сократить дробь, т. е. найти такие натуральные числа р и q, не имеющие общих
# делителей, что p/q = a/b.

def nod(x, y):
    while x != 0 and y != 0:
        if x > y: 
            x = x % y  
        else:
            y = y % x
    return x + y 


a = int(input('a: '))
b = int(input('b: '))

p = a / nod(a, b)
q = b / nod(a, b)

print(f'{p}/{q}={a}/{b}')  
