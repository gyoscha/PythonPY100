def func(grant, expenses):
    month = 0
    total_expenses = 0
    while month < 10:
        res = expenses - grant
        total_expenses = total_expenses +res
        expenses = expenses * 1.03
        month += 1

    return total_expenses

if __name__ == "__main__":
    # Write your solution here
    a = 6000
    b = 7000

    print(func(a, b))
