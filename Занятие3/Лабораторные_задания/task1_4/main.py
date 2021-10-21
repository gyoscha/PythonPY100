def sum_func(epsilon = 0.0001):
    n = 1
    sum_ = 1/n
    while sum_ > epsilon:
        sum_ += 1
        n += 1
if __name__ == "__main__":
    # Write your solution here
    print(sum_func())
