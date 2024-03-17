class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self) -> None:
        self.head:Node = None
        self.tail:Node = None
        self.length = 0
    def append(self,value):
        if isinstance(value,list):
            for i in value:
                self.append(i)
        else:
            node = Node(value)
            if self.head == None:
                self.head = node
                self.tail = node
                self.length+=1
            elif self.length == 1:
                self.head.next = node
                node.prev = self.head
                self.tail = node
                self.length+=1
            else:
                node.prev = self.tail
                self.tail.next = node
                self.tail = node
                self.length += 1

    def prepend(self,value):
        node = Node(value)
        if self.head == None:
            self.head = node
            self.tail = node
            self.length += 1
        elif self.length == 1:
            self.head.prev = node
            node.next = self.head
            self.tail = self.head
            self.head = node
            self.tail.prev = self.head
            self.length += 1
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.length += 1

    def insert(self,insert_index:int,value):
        node = Node(value)
        if insert_index > self.length:
            res = f"Insert index out of linked list length"
            print(res)
        elif insert_index == 0:
            self.prepend(value)
        elif insert_index == self.length:
            self.append(value)
        elif self.head == None:
            self.head = node
            self.tail = node
            self.length += 1
        elif self.length == 1:
            self.head.next = self.tail
            self.tail.next = node
            self.tail.prev = self.head
            node.prev = self.tail
            self.tail = node
            self.length += 1
# 
            # self.tail.next = node
            # self.tail.prev = self.head

            # node.prev = self.tail
            # self.tail = node

            # self.head.next = node
            # self.head.prev = None

            # self.length+=1
        # elif self.length == insert_index:
        #     if self.length == 0:
        #         self.head = node
        #         self.tail = node
        #         self.length += 1
        #     else:
        #         self.head.next = self.tail
        #         self.tail.prev = self.head
        #         self.length += 1
        else:
            current_node = self.head
            index = 0
            while index<insert_index-1:
                current_node = current_node.next
                index += 1
            node.next = current_node.next
            node.prev = current_node
            temp = current_node.next
            temp.prev = node
            current_node.next = node
    def traversal(self):
        if self.length == 0:
            res = f"There isn't any element in list"
            print(res)
        else:
            current_node = self.head
            temp = ''
            while current_node:
                temp+=f'{current_node.value}->'
                current_node = current_node.next
            print(temp.rstrip('->'))
    
    def reserve_traversal(self):
        last_node = self.tail
        temp = ''
        while last_node:
            temp+=f'{last_node.value}->'
            last_node = last_node.prev
        res = temp.rstrip('->')
        print(res)
    
    def get(self,index:int)->Node:
        if index>self.length:
            return f"Can't find index out of double linked list length "
        elif self.head:
            return f"There isn't any element in list"
        else:
            temp = self.head
            for _ in range(0,index):
                temp = temp.next
            return temp
    
    def pop_first(self):
        pop_node = self.head
        if self.length == 0:
            return False
        elif self.length == 1:
            self.delete()
        else:
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
        return pop_node.value
    
    def pop(self):
        pop_node = self.tail
        if self.length == 0:
            return False
        elif self.length == 1:
            self.delete()
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
        return pop_node.value

    # def search(self,value):
    #     flag = False
    #     temp = self.head
    #     for i in range(self.length):
    #         if temp.value == value:
    #             return  
    #         temp = temp.next
    def delete(self):
        self.head = None
        self.tail = None
        self.length = 0
    def remove(self,index:int)->Node:
        if self.length==0:
            res= f"There isn't any element in list"
            print(res)
        elif index>self.length-1:
            res= f"index is out of linked list range"
            print(res)
        else:
            if index==0:
                if self.length==1:
                    res = self.head
                    self.delete()
                    return res
                else:
                    res = self.head
                    self.head = self.head.next
                    self.head.prev = None
                    return res
            elif index==self.length-1:
                res = self.tail
                self.tail = self.tail.prev
                self.tail.next = None
                return res
            else:
                current_node = self.head
                run_time = 0
                while run_time<index-1:
                    current_node = current_node.next
                    run_time+=1
                res = current_node.next
                current_node.next = current_node.next.next
                current_node.next.prev = current_node
                return res
            
    def delete_node(self,index:int):
        if self.length==0:
            res= f"There isn't any element in list"
            print(res)
        elif index>self.length-1:
            res= f"index is out of linked list range"
            print(res)
        else:
            if index==0:
                if self.length==1:
                    self.delete()
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif index==self.length-1:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                current_node = self.head
                run_time = 0
                while run_time<index-1:
                    current_node = current_node.next
                    run_time+=1
                current_node.next = current_node.next.next
                current_node.next.prev = current_node

    def get(self,index:int)->Node:
        if index >= self.length:
            return False
        else:
            current_node = self.head
            for i in range(0,index):
                current_node = current_node.next
            return current_node

    def set(self,set_index:int,value):
        if set_index > self.length:
            print("Set index out of DLL length")
        else:
            current_node = self.head
            for _ in range(0,set_index):
                current_node = current_node.next

            current_node.value = value
    
dll = DoubleLinkedList()
# dll.append([1,2,3,4])
# dll.traversal()
# print(dll.reserve_traversal())
# dll.delete_node(4)
# dll.delete()
# dll.append(1)
# dll.append(2)
# dll.delete_node(1)
# print(dll.length)
# dll.insert(0,10)
dll.prepend(10)
dll.prepend(20)
dll.prepend(30)
dll.append(40)
dll.prepend(50)
dll.insert(5,100)
dll.traversal()
# print(dll.pop_first())
# print(dll.pop_first())
# print(dll.pop_first())
print(dll.pop())
print(dll.pop())
print(dll.pop())
dll.set(0,100)
dll.traversal()
print(dll.remove(2).value)
dll.traversal()
dll.reserve_traversal()
# my_doubly_linked_list = DoubleLinkedList()
# my_doubly_linked_list.append(7)

# print('Head:', my_doubly_linked_list.head.value)
# print('Tail:', my_doubly_linked_list.tail.value)
# print('Length:', my_doubly_linked_list.length)
