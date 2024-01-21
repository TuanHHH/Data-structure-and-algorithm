def reserve(array):
    for i in range(0,int(len(array)/2)):
        other = len(array)-i-1
        temp =array[i]
        array[i]=array[other]
        array[other] = temp
    print(array)
from array import *
my_array = array('i',[1,2,3,4,5])
reserve(my_array)

