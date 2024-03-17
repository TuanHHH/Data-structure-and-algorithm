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
        
class Queue:
    def __init__(self) -> None:
        self.Stack1 = Stack()
        self.Stack2 = Stack()

    def enqueue(self,value):
        self.Stack1.push(value)
    
    # def print_stack1(self):
    #     res = ''
    #     temp = 0
    #     while self.Stack1.isEmpty() == False:
    #         res+=f'{temp}:{self.Stack1.pop()}\n'
    #         temp+=1
    #     print('Stack1--------\n'+res+'-----------')


    # def print_stack2(self):
    #     res = ''
    #     temp = 0
    #     while self.Stack2.isEmpty() == False:
    #         res+=f'{temp}:{self.Stack2.pop()}\n'
    #         temp+=1
    #     print('Stack2--------\n'+res+'-----------')
    #     # print('Stack2'+res)


    def dequeue(self):
        if self.Stack1.isEmpty():
            return f'Queue is Empty'
        else:
            while self.Stack1.isEmpty() == False:
                current_stack1_value = self.Stack1.pop()
                self.Stack2.push(current_stack1_value)
            res = self.Stack2.pop()
            while self.Stack2.isEmpty() == False:
                current_stack2_value = self.Stack2.pop()
                self.Stack1.push(current_stack2_value)
            return res
    def peek(self):
        if self.Stack1.isEmpty():
            return f'Queue is Empty'
        else:
            while self.Stack1.isEmpty() == False:
                current_stack1_value = self.Stack1.pop()
                self.Stack2.push(current_stack1_value)
            res = self.Stack2.peek()
            while self.Stack2.isEmpty() == False:
                current_stack2_value = self.Stack2.pop()
                self.Stack1.push(current_stack2_value)
            return res
    def deleteQueue(self):
        self.Stack1.head = None
        self.Stack2.head = None
qu = Queue()
qu.enqueue(1)
qu.enqueue(2)
qu.enqueue(3)
print(qu.dequeue())
print(qu.peek())
print(qu.dequeue())
print(qu.dequeue())
print(qu.dequeue())