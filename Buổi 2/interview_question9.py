def allfib(n):
    for i in range(n):
        print(str(i)+':, '+str(fib(i)))

def fib(n):
    if n in [0,1]:
        return n
    else:
        return fib(n-1) + fib(n-2)
allfib(6)