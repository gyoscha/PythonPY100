
def func_2():
    min_list = int(min(list_new))
    for i, value in enumerate(list_new):
        if value == min_list:
            return i


if __name__ == "__main__":
    # Write your solution here
    N = 88972

    print('1. ', list(str(N)))

    list_new = list(str(N))
    for i, value in enumerate(list_new):
        list_new[i] = int(value)

    print('2. ', list_new)

    sum_even = 0
    for value in list_new:
        if value % 2 == 0:
            sum_even += value

    print('3. ', sum_even)

    print('4. ', len(list_new))

    print(f'5. Минимальная цифра - {min(list_new)}. Максимальная - {max(list_new)} ')

    print('6. ', list_new[1::2])

    a = len(list_new) - 1
    b = list_new[0] - list_new[a]
    print('7. ', b)

    min_list = int(min(list_new))
    for i, value in enumerate(list_new):
        if value == min_list:
            i
    print('8. ', i)
