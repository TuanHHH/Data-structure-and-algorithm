newTuple = ('a','b','c','d','e')

print(newTuple)
print(newTuple[1])
print(newTuple[-1])
print(newTuple[-2])
print(newTuple[1:3])
print(newTuple[:3])
print(newTuple[1:])
print(newTuple[:])
for i in newTuple:
    print(i)
for i in range(len(newTuple)):
    print(newTuple[i])
print('a' in newTuple)
print(newTuple.index('c'))
def searchTuple(p_tuple,element):
    for i in range(0,len(p_tuple)):
        if p_tuple[i]==element:
            return f'The {element} is not found at {i} index'
    return f'The element is not found'

print(searchTuple(newTuple,'b'))

myTuple = (1,4,3,2,5)
myTuple1 = (1,2,6,9,8,7)
print(myTuple+myTuple1)
print(myTuple*4)
print(myTuple.count(2))
print(tuple((1,2,3,4)))

list1 = [0,1,2,3,4,5,6,7]
list1[1]=3
print(list1)
list1 = [(1,2),(9,0),(3,4)]
tuple1= ([1,2],[3,4],[5,6])
print(list1)
print(tuple1)