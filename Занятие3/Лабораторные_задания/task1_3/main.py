def func_(a):
    list_ = []
    d = 2
    while d * d <= a:
        if a % d == 0:
            list_.append(d)
            a //= d
        else:
            d += 1
    if a > 1:
        list_.append(a)
    return list_


if __name__ == "__main__":
    # Write your solution here
    print(func_(33))
