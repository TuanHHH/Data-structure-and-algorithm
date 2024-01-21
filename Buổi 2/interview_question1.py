from array import *
def foo(array):
    sum = 0
    product = 0
    for i in array:
        sum += 1
    for i in array:
        product *= i
    print(f'Sum = {sum}, Product = {product} ')

my_array = array('i',[1,2,3,4])
foo(my_array)