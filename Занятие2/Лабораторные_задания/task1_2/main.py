a = int(input('Введите число А: '))
b = int(input('Введите числа В: '))

cond = a % 2 == 1 and b % 2 == 1

if cond:
    print('Нечетные')
else:
    print('Четные')
