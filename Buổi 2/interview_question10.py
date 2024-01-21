def powerOf2(n):
    if n<1:
        return 0
    elif n ==1:
        print(1)
        return 1
    else:
        perv = powerOf2(int(n/2))
        curr = perv*2
        print(curr)
        return(curr)
powerOf2(64)