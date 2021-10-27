def func_1(int_):
    int_list = [i for i in str(int_)]

    if len(int_list) == len(set(int_list)):
        print('Все цифры разные')
    else:
        print('Есть одинаковые')


if __name__ == "__main__":
    # Write your solution here
    print(func_1(123456789))
