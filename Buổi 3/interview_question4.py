def printUnorderedPairs(listA,listB):
    for i in range(len(listA)):
        for j in range(len(listB)):
            if listA[i]<listB[j]:
                print(str(listA[i])+','+str(listB[j]))
my_listA = [1,2,3]
my_listB = [2,1,8]
printUnorderedPairs(my_listA,my_listB)