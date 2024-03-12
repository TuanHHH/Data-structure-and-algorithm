class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self,new_node:Node):
        if isinstance(new_node,list) is True:
            for i in new_node:
                if self.head == None:
                    self.head = i
                    self.tail = i
                else:
                    self.tail.next = i
                    self.tail = i
                self.length += 1
        else:
            if self.head == None:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node
            self.length += 1

    def traversal(self):
        current_node = self.head
        ans = ""
        while current_node:
            ans +=f"{current_node.value}->"
            current_node = current_node.next
        return ans.rstrip("->")

    def get(self,index):
        if index<0 or index >= self.length:
            return False
        current = self.head
        for _ in range(0,index):
            current = current.next
        return current
        
def traversal_by_head(head:Node):
    current = head
    ans = ""
    while current:
        ans +=f"{current.value}->"
        current = current.next
    return ans.rstrip("->")

def intersection(head1:Node,head2:Node):
    ans = []
    while head2:
        temp = head1
        while temp:
            if temp == head2:
                ans.append(head2)
            temp = temp.next
        head2 = head2.next
    ans = [i.value for i in ans ]
    res=""
    for i in ans:
        res +=f'{i}->'
    return res.rstrip('->')

if __name__ == '__main__':
    newNode = Node(3)
    newNode1 = Node(1)
    newNode2 = Node(5)
    newNode3 = Node(9)


    newNode4 = Node(7)
    newNode5 = Node(2)
    newNode6 = Node(1)

    newNode7 = Node(2)
    newNode8 = Node(4)
    newNode9 = Node(6)

    link_list1 = LinkedList()
    link_list1.append([newNode,newNode1,newNode2,newNode3,newNode4,newNode5,newNode6])

    print(f'linked list 1: {link_list1.traversal()}')

    link_list2 = LinkedList()
    link_list2.append([newNode7,newNode8,newNode9,newNode4,newNode5,newNode6])
    print(f'linked list 2: {link_list2.traversal()}')
    print(intersection(newNode,newNode7))