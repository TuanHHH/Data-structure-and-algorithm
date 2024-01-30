def reversing_inplace_array(lst:list):
    for i in range(len(lst)//2):
        temp = lst[len(lst)-1-i]
        lst[len(lst)-1-i] = lst[i]
        lst[i] = temp
    return lst
print(reversing_inplace_array([1,2,3,4,5]))
