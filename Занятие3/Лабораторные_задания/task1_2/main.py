def factorial(n):
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1
    return factorial

if __name__ == "__main__":
    # Write your solution here
    print(factorial(4))
