# 1. Create an list and traverse.
def traverse(list):
    for i in list:
        print(i)
# 2. Access individual elements through indexes
def accessThroughIndex(list, index):
    print(list[index])
# 3. Append any value to the list using append() method
def appendToList(list, value):
    list.append(value)
# 4. Insert value in an list using insert() method
def insertToList(list, value):
    # insert to first 0/ insert to last 1
    list.insert(0, value)
# 5. Extend python list using extend method
def extendList(list, newList):
    list.extend(newList)
# 6. Add items from list into list
def addItems(list, items):
    list.extend(items)
# 7. Remove any list element using remove() method
def removeList(list, value):
    list.remove(value)
# 8. Remove last list element using pop() method
def removeLastOfList(list):
    list.pop()
# 9. Fetch any element through its index using index() method
def findIndex(list, value):
    return list.index(value)
# 10. Reverse a python list using reverse() method
def reverseList(list):
    list.reverse()

# 11. Check for number of occurrences of an element using count() method
def countInList(list, value):
    return list.count(value)

# 12. Append a string to char list 
def appendStringToCharList(list, tmpStr:str):
    list.append(tmpStr)

# 13. Slice Elements from an list
def sliceList(list, firstEl, lastEl):
    return list[firstEl:lastEl]



if __name__ == '__main__':
    my_list = [1,2,3,4,5,6,7,8,1,2,3,1]
    traverse(my_list)
    appendToList(my_list,10)
    print(my_list)

    insertToList(my_list,20)
    print(my_list)

    removeList(my_list,2)
    print(my_list)

    removeLastOfList(my_list)
    print(my_list)
    print(findIndex(my_list,7))

    reverseList(my_list)
    print(my_list)

    print(countInList(my_list,1))

    print(sliceList(my_list,2,6))