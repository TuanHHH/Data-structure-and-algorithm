my_dict = {'a':5,'b':9,'c':2}
def max_value_key(my_dict:dict)->dict:
    return max(list(my_dict.values()))
print(max_value_key(my_dict))