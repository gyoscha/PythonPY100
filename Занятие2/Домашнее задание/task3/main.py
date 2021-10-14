a = int(input('Введите число A: '))
b = int(input('Введите число B: '))
c = int(input('Введите число C: '))

res_1 = a < 45 and b >= 45 and c >= 45
res_2 = a >= 45 and b < 45 and c >= 45
res_3 = a >= 45 and b >= 45 and c < 45

if res_1 or res_2 or res_3:
    print('True')   # только одно число меньше 45
else:
    print('False')
