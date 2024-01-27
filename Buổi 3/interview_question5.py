def printUnorderedPairs(arrayA,arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            for k in range(0,100000):
                print(str(arrayA[i])+','+str(arrayB[j]))
my_listA = [1,2,3]
my_listB = [1,2,3]
printUnorderedPairs(my_listA,my_listB)
