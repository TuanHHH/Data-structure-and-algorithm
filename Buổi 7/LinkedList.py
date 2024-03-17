class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def append(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert(self,insert_index:int,value):
        if insert_index < 0 or insert_index > self.length:
            return False
        else:
            if insert_index == 0:
                self.prepend(value)
            elif insert_index == self.length:
                self.append(value)
            else:
                current_index = 0
                new_node = Node(value)
                temp_node = self.head
                while True:
                    current_index += 1
                    if current_index < insert_index:
                        temp_node = temp_node.next
                    elif current_index >= insert_index:
                        break

                new_node.next = temp_node.next
                temp_node.next = new_node
                self.length += 1

    def traversal(self):
        temp = 'Linked list:'
        current_node = self.head
        while current_node:
            temp += f'{current_node.value}->'
            current_node = current_node.next
        print(temp.rstrip('->'))
    
    def delete(self):
        self.head = None
        self.tail = None
        self.length = 0

    def search(self,target):
        current = self.head
        while current:
            if current.value == target:
                return True
            current = current.next
        return False

    def get_value(self,index):
        if index<0 or index >= self.length:
            return False
        current = self.head
        for _ in range(0,index):
            current = current.next
        return current.value

    def get(self,index):
        if index<0 or index >= self.length:
            return False
        current = self.head
        for _ in range(0,index):
            current = current.next
        return current

    def set_value(self,index,value):
        if index < 0 or index >= self.length:
            print('Vượt quá độ dài linked list nên không thể thay đổi giá trị')
        else:
            if index == 0:
                self.head.value = value
            elif index == self.length-1:
                self.tail.value = value
            else:
                temp = self.head
                current_index = 0
                while current_index <= index - 1:
                    temp = temp.next
                    current_index += 1
                temp.value = value
                
    def remove(self,remove_index):
        if remove_index >= self.length or remove_index < 0:
            return None
        elif remove_index == 0:
            self.pop_first()
        else:
            if remove_index == self.length - 1:
                self.pop_last()
            else:
                current = self.head
                for _ in range(1,remove_index):
                    current = current.next
                current.next = current.next.next
                self.length -= 1

    def pop_first(self):
        if self.length == 0:
            return None
        else:
            self.head = self.head.next
            self.length -= 1

    def pop_last(self):
        temp = self.head
        if self.length != 1:
            for _ in range(0,self.length-2):
                temp = temp.next
            self.tail = temp
            self.tail.next = None 
            self.length -= 1
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
        elif self.length == 0:
            return None
    def reserve(self):
        current_node = self.head
        prev_node = None
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head, self.tail = self.tail, self.head
if __name__ == "__main__":
    new_linked_list = LinkedList()
    new_linked_list.prepend(9)
    new_linked_list.append(10)
    new_linked_list.append(100)
    new_linked_list.append(11)
    new_linked_list.append(1)
    new_linked_list.append(2)
    new_linked_list.append(3)
    new_linked_list.append(4)
    new_linked_list.prepend(10)
    new_linked_list.prepend(20)
    print('ddo dang',new_linked_list.length)
    new_linked_list.insert(10,11)
    # new_linked_list.traversal()
    # # new_linked_list.delete()
    # new_linked_list.traversal()
    # print(new_linked_list.search(908))
    # print(new_linked_list.head.value)
    # print(new_linked_list.get(7))
    # print('heelo')
    # new_linked_list.set_value(1,0)
    # print(new_linked_list.head.value)
    # print(new_linked_list.tail.value)
    # new_linked_list.pop_first()
    print('ddo dang',new_linked_list.length)
    new_linked_list.traversal()
    new_linked_list.remove(8)
    # print(new_linked_list.get(0))
    print('ddo dang',new_linked_list.length)
    new_linked_list.traversal()
    # new_linked_list.reserve()
    new_linked_list.traversal()
    # new_linked_list.remove(7)

    # print(new_linked_list.get(8))
    # new_linked_list.traversal()
    # print(new_linked_list.head.value)
    # print(new_linked_list.tail.value)
    # print('ddo dang',new_linked_list.length)
