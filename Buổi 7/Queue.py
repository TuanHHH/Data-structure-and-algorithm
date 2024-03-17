class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

class Queue:
    def __init__(self) -> None:
        self.LinkedList = LinkedList()

    def isEmpty(self):
        return self.LinkedList.head == None
    
    def enqueue(self,value):
        node = Node(value)
        # self.LinkedList.tail.next = node
        # self.LinkedList.tail = node
        # self.LinkedList.head.next = node
        if self.LinkedList.head == None and self.LinkedList.tail == None:
            self.LinkedList.head = node
            self.LinkedList.tail = node
        else:
            self.LinkedList.tail.next = node
            self.LinkedList.tail = node

    def dequeue(self):
        if self.isEmpty():
            return "There isn't any element in queue"
        else:
            node_value = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return node_value

    def peek(self):
        if self.isEmpty():
            return "There isn't any element in queue"
        else:
            node_value = self.LinkedList.head.value
            return node_value
    def deleteQueue(self):
        self.LinkedList.head = None
        self.LinkedList.tail = None
qu = Queue()
qu.enqueue(1)
qu.enqueue(2)
qu.enqueue(3)
qu.enqueue(4)
print(qu.dequeue())
qu.enqueue(5)
print(qu.dequeue())
print(qu.dequeue())
print(qu.dequeue())
print(qu.dequeue())
print(qu.dequeue())
print(qu.dequeue())