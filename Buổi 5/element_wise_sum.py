tuple1 = (1,2,3)
tuple2 = (4,5,6)
def tuple_elementwise_sum(tuple1,tuple2):
    res = tuple()
    for i,v in enumerate(tuple1):
        res+= (v+tuple2[i],)
    return res
output_tuple = tuple_elementwise_sum(tuple1,tuple2)
print(output_tuple)