from array import *
def printPairs(array):
    for i in array :
        for j in array:
            print(str(i)+','+str(j))
my_array = array('i',[1,2,3])
printPairs(my_array)