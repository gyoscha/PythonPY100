if __name__ == "__main__":
    # Write your solution here
    list_ = [88, 70, 90, 8, 24, 21, 150, 65, 91, 76]
    list_max = max(list_)

    for i, value in enumerate(list_):
        if value == list_max:
            list_[i] = list_[0]
            list_[0] = list_max

    print(list_)









