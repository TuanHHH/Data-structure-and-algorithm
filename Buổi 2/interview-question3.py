def printUnorderedPairs(array):
    for i in range(0,len(array)):
        for j in range(i+1,len(array)):
            print(str(array[i])+","+str(array[j]))
from array import *
my_array= array('i',[1,2,3,4])
printUnorderedPairs(my_array)