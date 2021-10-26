def func():
    print(len([i for i in range(n, m) if i % 2 == 0]))

if __name__ == "__main__":
    # Write your solution here
    n = 1
    m = 5
    print(func())
