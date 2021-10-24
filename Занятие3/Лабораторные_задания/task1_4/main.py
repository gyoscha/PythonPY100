def sum_func(epsilon = 0.0001):
    n = 2
    sum_ = 1/n
    while sum_ > epsilon:
        sum_ += 1/(2 ** n)
        n += 1
    return n


if __name__ == "__main__":
    # Write your solution here
    print(sum_func())
