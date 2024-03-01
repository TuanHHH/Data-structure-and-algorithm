def get_diagonal(input_tuple):
    res = tuple()
    column_index = 0
    for my_tuple in input_tuple:
        if isinstance(my_tuple,tuple):
            res += (my_tuple[column_index],)
            column_index +=1
    return res

input_tuple = (
    (1,2,3),
    (4,5,6),
    (7,8,9)
)
output_tuple = get_diagonal(input_tuple)
print(output_tuple)