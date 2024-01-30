dict1 ={'a':1,'b':2,'c':3}
dict2 = {'b':3,'c':4,'d':5}
def merge_dicts(dict1:dict,dict2:dict):
    assert isinstance(dict1,dict) and isinstance(dict2,dict), f'2 parameters must be dictionary'
    res_dict ={}
    res_dict.update(dict1)
    for k1,v1 in dict1.items():
        for k2, v2 in dict2.items():
            if k1 == k2:
                res_dict[k1] += dict2[k2]
    
    for k2 in dict2:
        if k2 not in res_dict:
            res_dict[k2] = dict2[k2]

    return res_dict
print(merge_dicts(dict1,dict2))