# 1. Create an list and traverse.
def traverse(list):
    for i in list:
        print(i)
# 2. Access individual elements through indexes
def accessThroughIndex(list, index):
    print(list[index])
# 3. Append any value to the list using append() method
def appendToArray(list, value):
    list.append(value)
# 4. Insert value in an list using insert() method
def insertToArray(list, value):
    # insert to first 0/ insert to last 1
    list.insert(0, value)
# 5. Extend python list using extend method
def extendArray(list, newArray):
    list.extend(newArray)
# 6. Add items from list into list using fromlist() method
def addItems(list, items):
    list.fromlist(items)
# 7. Remove any list element using remove() method
def removeArray(list, value):
    list.remove(value)
# 8. Remove last list element using pop() method
def removeLastOfArray(list):
    list.pop()
# 9. Fetch any element through its index using index() method
def findIndex(list, value):
    return list.index(value)
# 10. Reverse a python list using reverse() method
def reverseArray(list):
    list.reverse()

# 11. Check for number of occurrences of an element using count() method
def countInArray(list, value):
    return list.count(value)

# 12. Append a string to char list using fromstring() method
def appendStringToCharArray(list, tmpStr):
    list.fromunicode(tmpStr)
    return list
# 13. Slice Elements from an list
def sliceArray(list, firstEl, lastEl):
    return list[firstEl:lastEl]



if __name__ == '__main__':
    my_list = [1,2,3,4,5,6,7,8,1,2,3,1]
    traverse(my_list)
    appendToArray(my_list,10)
    print(my_list)

    insertToArray(my_list,20)
    print(my_list)

    removeArray(my_list,2)
    print(my_list)

    removeLastOfArray(my_list)
    print(my_list)
    print(findIndex(my_list,7))

    reverseArray(my_list)
    print(my_list)

    print(countInArray(my_list,1))

    print(sliceArray(my_list,2,6))