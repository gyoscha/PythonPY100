if __name__ == "__main__":
    # постарайтесь не использовать "магические" числа,
    # а по возможности дать переменным осмысленные названия и использовать их
    lesenka = 'Hello, world'

    for index, value in enumerate(lesenka, start=5):
        index = ' ' * index   # пробел умножаю на индекс: 5, 6 и тд
        print(index, value)   # 5 пробелов + значение
