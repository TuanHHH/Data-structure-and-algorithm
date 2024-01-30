def reversion_integer(num:int):
    assert isinstance(num,int), f'The number must be an integer'
    reverse_num = 0
    while num>0:
        reverse_num = reverse_num * 10
        reverse_num += num % 10
        num = num // 10
    return reverse_num
print(reversion_integer(1234567))