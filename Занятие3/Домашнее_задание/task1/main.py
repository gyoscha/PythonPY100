def func_():
    a = [int(i) for i in input('Введите последовательность чисел через запятую: ').split(',')]
    list_numbers = []
    for value in a:
        if 3 <= value <= 13 and value > 0:
            list_numbers.append(value)
    return list_numbers


if __name__ == "__main__":
    # Write your solution here
    print(func_())
