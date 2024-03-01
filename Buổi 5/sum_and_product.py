def sum_product(input_tuple:tuple)->tuple:
    sum_result = sum(input_tuple)
    product_result = 1
    for i in input_tuple:
        product_result *= i
    return sum_result, product_result
input_tuple = (1,2,3,4)
sum_result, product_result = sum_product(input_tuple)
print(sum_result, product_result)