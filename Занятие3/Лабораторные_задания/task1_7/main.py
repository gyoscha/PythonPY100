def func(savings, grant, expenses):
    month = 0
    diff_expenses = 0
    while savings > diff_expenses:
        res = expenses - grant
        diff_expenses += res
        expenses = expenses * 1.05
        month += 1
    return month

if __name__ == "__main__":
    # Write your solution here
    a = 100000
    b = 6000
    c = 9000

    print(func(a, b, c))
