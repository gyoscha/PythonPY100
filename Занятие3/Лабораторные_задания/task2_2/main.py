def func_():
    c = input('Введите слово: ')
    if c != c[::-1]:
        print('Это не палиндром')
    else:
        print('Это палиндром')
    return c[::-1]

if __name__ == "__main__":
    # Write your solution here
    print(func_())
