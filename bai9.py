def gcd(a:int, b:int):
    assert a>=0 and b>=0 and isinstance(a,int) and isinstance(b,int), f'The 2 input value must be positive integer only'
    if a<b:
        a, b = b,a
    if b==0:
        return a
    else:
        return gcd(b,a%b)

print(gcd(12,3))