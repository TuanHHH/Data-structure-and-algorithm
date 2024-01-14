def powerOfTwo(n):
    if n == 0:
        return 1
    else:
        return powerOfTwo(n-1)*2
print(powerOfTwo(3))