class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

class Stack:
    def __init__(self) -> None:
        self.LinkedList = LinkedList()

    def isEmpty(self):
        return self.LinkedList.head == None
    
    def peek(self):
        if self.isEmpty():
            return 'There is not any element in stack'
        else:
            nodeValue = self.LinkedList.head.value
            return nodeValue
        
    def push(self,value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node

    def pop(self):
        if self.isEmpty():
            return "There is not any element in stack"
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue
        
st = Stack()
print(st.isEmpty())
st.push(1)
st.push(2)
st.push(3)
st.push(4)
print(st.isEmpty())
print(st.peek())
print(st.pop())
print(st.pop())
print(st.pop())
print(st.pop())
print(st.pop())
