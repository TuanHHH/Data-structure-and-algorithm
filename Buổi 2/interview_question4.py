def printUnorderedPairs(arrayA,arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            if arrayA[i]<arrayB[j]:
                print(str(arrayA[i])+','+str(arrayB[j]))
from array import *
my_arrayA = array('i',[1,2,3])
my_arrayB = array('i',[2,1,8])
printUnorderedPairs(my_arrayA,my_arrayB)