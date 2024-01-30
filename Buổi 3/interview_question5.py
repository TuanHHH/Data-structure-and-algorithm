def printUnorderedPairs(listA,listB):
    for i in range(len(listA)):
        for j in range(len(listB)):
            for k in range(0,100000):
                print(str(listA[i])+','+str(listB[j]))
my_listA = [1,2,3]
my_listB = [1,2,3]
printUnorderedPairs(my_listA,my_listB)
