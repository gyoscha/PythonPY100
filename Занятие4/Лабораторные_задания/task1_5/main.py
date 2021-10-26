def func():
    list_new = len([i for i in list_ if i % 2 == 0])   # Четные
    list_new_1 = len([i for i in list_ if i % 2 == 1])   # Нечетные

    if list_new > list_new_1:
        print('Четных больше')
        return list_new
    elif list_new < list_new_1:
        print('Нечетных больше')
        return list_new_1
    else:
        print('Одинаково')


if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]

    print(func())
