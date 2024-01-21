from array import *
def twoSum(nums,target):
    flag = -1
    for index1, value1 in enumerate(nums):
        for index2, value2 in enumerate(nums):
            if(index1 == index2):
                continue
            else:
                if(value1+value2 == target):
                    print(value1,value2)
                    return [index1,index2]
    return flag
my_array = array('i',[3,2,1,3])
target = 6
print(twoSum(my_array,target))
