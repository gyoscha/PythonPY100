wind = int(input())

if 1 <= wind <= 4:
    print('слабый')
elif 5 <= wind <= 10:
    print('умеренный')
elif 11 <= wind <= 18:
    print('сильный')
elif wind > 19:
    print('ураганный')
