def decimalToBinary(n:int):
    assert n>=0 and isinstance(n,int), f'The number must be positive integer'
    if n/2 == 0:
        return 0
    else:
        return 10 * decimalToBinary(int(n/2)) + n%2
    
print(decimalToBinary(8))