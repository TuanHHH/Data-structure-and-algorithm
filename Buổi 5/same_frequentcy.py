def check_same_frequency(list1:list,list2:list)->bool:
    unique_value_in_list1 = set(list1)
    unique_value_in_list2 = set(list2)
    if unique_value_in_list1 != unique_value_in_list2:
        return False
    else:
        f_list1 = {elem:list1.count(elem) for elem in unique_value_in_list1}
        f_list2 = {elem:list2.count(elem) for elem in unique_value_in_list2}
        print(f_list1,f_list2)
        if f_list1 == f_list2:
            return True
        else:
            return False
list1 = [1,2,3,2,1]
list2 = [3,1,2,1,3]
print(check_same_frequency(list1,list2))