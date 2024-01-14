def power(n:int, k:int):
    assert n>=0 and isinstance(float(n),float), f'The number must be positive number'
    assert k>0 and isinstance(k,int), f'The number of exponent must be greater than 0 and is integer'
    if k == 1:
        return n
    else:
        return n*power(n,k-1)
print(power(2,4))