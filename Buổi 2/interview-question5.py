def printUnorderedPairs(arrayA,arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            for k in range(0,100000):
                print(str(arrayA[i])+','+str(arrayB[j]))
from array import *
my_arrayA = array('i',[1,2,3])
my_arrayB = array('i',[1,2,3])
printUnorderedPairs(my_arrayA,my_arrayB)
