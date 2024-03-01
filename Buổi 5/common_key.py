def merge_dict(dict1,dict2):
    res = dict(dict1)
    res.update(dict2)
    res = {key:0 for key in res.keys()}
    for key in res.keys():
        if key not in dict1.keys():
            res[key] = dict2[key]
        elif key not in dict2.keys():
            res[key] = dict1[key]
        elif key in dict1.keys() and dict2.keys():
            res[key] = dict1[key] + dict2[key]
    return res

d1={'a':1,'b':2,'c':3}
d2={'b':3,'c':4,'d':5}
print(merge_dict(d1,d2))