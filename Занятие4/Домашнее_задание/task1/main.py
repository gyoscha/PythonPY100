def func_1(int_):
    int_list = [i for i in str(int_)]

    if len(set(int_list)) == 1:
        print('Одинаковые')
    else:
        print('Разные')


if __name__ == "__main__":
    # Write your solution here
    print(func_1(1199999999))
