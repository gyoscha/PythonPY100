def func_():
    a = [int(i) for i in input('Введите последовательность чисел через запятую: ').split(',')]
    sum_ = 0
    for value in a:
        if value != 0 and value > 0:
            sum_ += value
    return sum_


if __name__ == "__main__":
    # Write your solution here
    print(func_())
