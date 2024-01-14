def factorial(n):
    assert n >= 0 and  int(n) == n, f'The number must be positive integer only'
    if n in [0,1]:
        print(n)
        return 1
    else:
        print(n)
        return factorial(n-1)*n
        
print(factorial(3))