
# filtered_dict = filter_dict(my_dict,lambda k,v:v%2==0)
def filter_dict(my_dict:dict,lambda_funtion)->dict:
    d={}
    res = tuple()
    for k,v in my_dict.items():
        if lambda_funtion(k,v):
            d[k]=v
    print(res)
    return d
my_dict = {'a':1,'b':2,'c':3,'d':4}
filtered_dict = filter_dict(my_dict,lambda k,v:v % 2 == 0)
print(filtered_dict)
