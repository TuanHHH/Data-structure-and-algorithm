def printUnorderedPairs(list):
    for i in range(0,len(list)):
        for j in range(i+1,len(list)):
            print(str(list[i])+","+str(list[j]))
my_list= [1,2,3,4]
printUnorderedPairs(my_list)