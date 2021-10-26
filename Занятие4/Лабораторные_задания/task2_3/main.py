if __name__ == "__main__":
    # Write your solution here
    num_1 = 789

    digits_list = [int(i) for i in str(num_1)]

    sum_digits_list = [int(i) for i in str(sum(digits_list))]

    if len(sum_digits_list) == 2:
        print('True')
    else:
        print('False')