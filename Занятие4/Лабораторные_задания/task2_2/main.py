if __name__ == "__main__":
    # Write your solution here
    num_1 = 11

    digits_list = [int(i) for i in str(num_1)]

    if (4 in digits_list and 8 in digits_list) or 9 in digits_list:
        print('True')
    else:
        print('False')
