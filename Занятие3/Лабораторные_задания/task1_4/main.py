def sum_func(epsilon=0.0001):
    n = 1
    sum_ = 0
    item_n = 1 / 2 ** n   # очередной элемент
    while item_n >= epsilon:
        sum_ += item_n
        n += 1
        item_n = 1 / 2 ** n   # Перезаписываем элемент, чтобы он не был одинаковым.

    return sum_

# можно сделать по-другому:

def sum_func_1(epsilon=0.0001):
    n = 1
    sum_ = 0
    while True:
        item_n = 1 / 2 ** n
        if item_n < epsilon:
            break
        sum_ += item_n
        n += 1


    return sum_

if __name__ == "__main__":
    # Write your solution here
    print(sum_func())
