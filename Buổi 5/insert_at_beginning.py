def insert_value_front(input_tuple:tuple,value_to_insert:int)->tuple:
    res = tuple((value_to_insert,)) + input_tuple
    return res

input_tuple = (2,3,4)
value_to_insert = 1
output_tuple = insert_value_front(input_tuple,value_to_insert)
print(output_tuple)