def func_():
    num_1 = int(input('Введите число: '))
    num_str = str(num_1)

    if num_str != num_str[::-1]:
        print('Это не палиндром')
    else:
        print('Это палиндром')
    return num_str[::-1]


if __name__ == "__main__":
    # Write your solution here
    print(func_())
