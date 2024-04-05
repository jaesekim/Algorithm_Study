n = int(input())


def fibonacci(num):
    if not num or num == 1:
        return num
    return fibonacci(num - 2) + fibonacci(num - 1)

print(fibonacci(n))
