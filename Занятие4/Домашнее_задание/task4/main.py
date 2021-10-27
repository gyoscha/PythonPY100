def happy_ticket(num):
    num_list = [i for i in str(num)]
    if sum([int(i) for i in num_list[:3]]) == sum([int(i) for i in num_list[3:]]):
        print("Счастливый")
    else:
        print("Обычный")


if __name__ == "__main__":
    # Write your solution here
    happy_num = int(input('Введите число: '))
    print(happy_ticket(happy_num))
