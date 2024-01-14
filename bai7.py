def sumOfDigit(n):
    assert n>=0 and int(n)==n, f'The number must be positive integer only'
    if int(n/10) == 0:
        return n%10
    else:
        return sumOfDigit(int(n/10))+n%10
print(sumOfDigit(34))