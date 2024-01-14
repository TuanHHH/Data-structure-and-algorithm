def fibonacci(n):
    assert n >= 0 and int(n) == n, f'The number must be positive integer only'
    if n in [1,2]:
        # print(n)
        return 1
    else:
        print(n)
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(4))