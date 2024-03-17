class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

class Stack:
    def __init__(self) -> None:
        self.stack = LinkedList()
        self.min_value = None

    def push(self,value):
        node = Node(value)
        node.next = self.stack.head
        self.stack.head = node

    def pop(self):
        if self.stack.head == None:
            return 'there nothing in the stack'
        else:
            node_value = self.stack.head.value
            self.stack.head = self.stack.head.next
            return node_value
        
    def peek(self):
        if self.stack.head == None:
            return 'there nothing in the stack'
        else:
            node_value = self.stack.head.value
            return node_value
        

    def find_stack_min(self):
        if self.stack.head != None:
            temp_list = []
            while self.stack.head != None:
                temp_list.append(self.pop())
            res = min(temp_list)
            while len(temp_list):
                self.push(temp_list.pop())
            return res
        else:
            return "There is not any element in the stack"
st = Stack()

st.push(5)
print(st.find_stack_min())
st.push(6)  
print(st.find_stack_min())
st.push(3)
print(st.find_stack_min())
st.push(7)
print(st.find_stack_min())
st.pop()
print(st.find_stack_min())
st.pop()
print(st.find_stack_min())
