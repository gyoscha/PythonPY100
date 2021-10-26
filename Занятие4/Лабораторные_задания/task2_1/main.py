def sum_2():
    sum_even = 0
    for value in list_new:
        if value % 2 == 0:
            sum_even += value

    return sum_even


def func_1():
    a = len(list_new) - 1
    b = list_new[0] - list_new[a]

    return b


def func_2():
    min_list = int(min(list_new))
    for i, value in enumerate(list_new):
        if value == min_list:
            return i


if __name__ == "__main__":
    # Write your solution here
    N = 88972

    list_new = list(str(N))
    for i, value in enumerate(list_new):
        list_new[i] = int(value)

    print('1. ', list(str(N)))
    print('2. ', list_new)
    print('3. ', sum_2())
    print('4. ', len(list_new))
    print(f'5. Минимальная цифра - {min(list_new)}. Максимальная - {max(list_new)} ')
    print('6. ', list_new[1::2])
    print('7. ', func_1())
    print('8. ', func_2())
