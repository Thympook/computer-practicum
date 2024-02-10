# Даны два натуральных числа. Выяснить, является ли хоть одно из них палиндромом, 
# т. е. таким числом, десятичная запись которого читается одинаково слева направо и
# справа налево.
# (Определить функцию, позволяющую распознавать числа-палиндромы до 1010)


def is_palindrome(num): 
    num = str(num) 
    return num == num[::-1] 

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))

if is_palindrome(num1) and is_palindrome(num2):
    print('Оба числа - палиндромы')
elif is_palindrome(num1) or is_palindrome(num2):
    print('Одно из чисел - палиндром')
    if is_palindrome(num1):
        print(num1)
    else:
        print(num2)
else:
    print('Палиндромов нет')
