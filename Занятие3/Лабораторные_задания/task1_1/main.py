def main():
    a = 0
    b = 0
    count_ = 0
    while (a ** 2 + b ** 2) < 500:
        a += 1
        b += 1
        count_ += 1
    return count_



if __name__ == "__main__":
    # Write your solution here
    print(main())
