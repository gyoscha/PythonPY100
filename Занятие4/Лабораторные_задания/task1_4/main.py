def func():
    list_old = range(n, m)
    list_new = [i for i in list_old if i > sum(list_old) / len(list_old)]

    return list_new


if __name__ == "__main__":
    # Write your solution here
    n = 1
    m = 10
    print(func())
