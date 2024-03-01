class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value) -> None:
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1
    
    
    def append(self,value):
        newNode = Node(value)
        self.tail.next = newNode
        self.tail = newNode
        self.length += 1

    def prepend(self,value):
        newNode = Node(value)
        temp = self.head
        self.head = newNode
        self.head.next = temp
        self.length += 1

    def insert(self,insertIndex:int,value):
        newNode = Node(value)
        if insertIndex>= 0 and insertIndex <= self.getLength():
            if insertIndex == 0:
                self.prepend(value)
            elif insertIndex == self.getLength():
                self.append(value)
            else:
                temp = self.head
                index = 0
                while index <= insertIndex-1:
                    temp = temp.next
                    index += 1
                    if index == insertIndex -1:
                        temp_address = temp.next
                        temp.next = newNode
                        temp = temp_address
                        break
                newNode.next = temp
                self.length += 1

    def delete(self, deleteIndex):
        index = 0
        temp = self.head
        if deleteIndex == 0:
            self.head = self.head.next
            self.length -= 1

        while index <= deleteIndex:
            if deleteIndex == self.getLength() - 1:
                if index == self.getLength()-2:
                    self.tail = temp
                    temp.next = None
                    self.length -= 1
                    break

            elif index == deleteIndex-1:
                temp.next = temp.next.next
                self.length -= 1

            index += 1
            temp = temp.next


    def change_value(self,changeIndex:int,value):
        if changeIndex == 0:
            self.head.value = value
        elif changeIndex == self.getLength()-1:
            self.tail.value = value
        elif changeIndex < 0 or changeIndex >= self.getLength():
            raise Exception('Phải trong khoảng giá trị của LinkedList')
        else:
            temp = self.head
            index = 0
            while index <= changeIndex-1:
                temp = temp.next
                index += 1
            temp.value = value

    def print_link_list(self):
        temp = self.head
        index = 0
        while temp:
            print(f'Phần tử thứ {index}:{temp.value}')
            temp = temp.next
            index += 1

    def getLength(self):
        return self.length

new_linked_list = LinkedList(10)

new_linked_list.append(11)

new_linked_list.append(12)

new_linked_list.append(13)
new_linked_list.append(14)
new_linked_list.append(10)

new_linked_list.prepend(1)
new_linked_list.change_value(4,1100)
new_linked_list.insert(4,3000)

new_linked_list.delete(7)
new_linked_list.delete(4)
new_linked_list.delete(4)
print(f'Mảng có độ dài là {new_linked_list.getLength()}')
new_linked_list.print_link_list()