if __name__ == "__main__":
    # Write your solution here
    num_1 = 9854

    digits_list = [int(i) for i in str(num_1)]
    print(digits_list)

    if sum(digits_list) % 7 == 0:
        print('True')
    else:
        print('False')
