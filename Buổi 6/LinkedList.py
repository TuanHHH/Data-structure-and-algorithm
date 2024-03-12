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
        if isinstance(value,list) is True:
            for i in value:
                new_node = Node(i)
                if self.head == None:
                    self.head = new_node
                    self.tail = new_node
                else:
                    self.tail.next = new_node
                    self.tail = new_node
                self.length += 1
        else:
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
                for _ in range(insert_index-1):
                    temp_node = temp_node.next

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
    
    def middle_of_singly_linked_list(self):
        if self.tail == self.head:
            return self.head
        else:
            return self.get_value(self.length//2)
        
    def remove_duplicates(self):
        if self.head == None:
            return
        else:
            current_node = self.head
            node_values = set()
            node_values.add(current_node.value)
            while current_node.next:
                if current_node.next.value in node_values:  # duplicate found
                    current_node.next = current_node.next.next
                    self.length -= 1
                else:
                    node_values.add(current_node.next.value)
                    current_node = current_node.next
            self.tail = current_node

    def remove_linked_list_element(self,value):
        index = 0
        for _ in range(0,self.length):
            if self.get_value(index)==value:
                self.remove(index)
                index -= 1
            index+=1

    def is_palindrome_linked_list(self)->bool:
        for i in range(0,self.length//2+1):
            if self.get_value(i) != self.get_value(self.length-i-1):
                return False
        return True

    def swap_value(self,index1:int,index2:int):
        if index1 < 0 or index2 <0 or index1>= self.length or index2 >= self.length:
            return False
        elif index1 == index2:
            return
        else:
            if index1 > index2:
                index1, index2 = index2, index1
            
            if index1 == 0 and index2 == self.length -1:
                before_node2 = self.get(index2-1)
                before_node2.next = self.head
                self.head.next,self.tail.next = self.tail.next, self.head.next
                self.head, self.tail = self.tail, self.head

            elif index1 ==0:
                node2 = self.get(index2)
                before_node2 = self.get(index2-1)

                f_node = self.head
                before_node2.next = f_node

                f_node.next, node2.next = node2.next, f_node.next
                self.head = node2

            elif index2 == self.length-1:
                node1 = self.get(index1)
                node2 = self.tail
                before_node1 = self.get(index1-1)
                before_node2 = self.get(index2-1)

                before_node1.next, before_node2.next = before_node2.next, before_node1.next

                node2.next = node1.next

                self.tail = node1
                self.tail.next = None
            
            else:
                node1 = self.get(index1)
                node2 = self.get(index2)
                before_node1 = self.get(index1-1)
                before_node2 = self.get(index2-1)
                before_node1.next, before_node2.next = before_node2.next, before_node1.next
                node1.next, node2.next = node2.next, node1.next

    def find_nth_to_last_element(self,index:int):
        if index < 1 or index > self.length:
            return False
        else:
                current_node = self.head
                for _ in range(self.length - index):
                    current_node = current_node.next
        return current_node.value

def merge_2_sorted_linked_list(linked_list1:LinkedList,linked_list2:LinkedList)->LinkedList:
    ans = LinkedList()
    i = j = 0
    while i < linked_list1.length and j < linked_list2.length:
        if linked_list1.get_value(i)<linked_list2.get_value(j):
            ans.append(linked_list1.get_value(i))
            i+=1
        else:
            ans.append(linked_list2.get_value(j))
            j+=1
    return ans

def sum_list(link_list1:LinkedList,link_list2:LinkedList)->LinkedList:
    link_list1.reserve()
    link_list2.reserve()
    list1_number = 0
    for i in range(link_list1.length):
        list1_number = list1_number*10 +link_list1.get_value(i)
    list2_number = 0
    for i in range(link_list2.length):
        list2_number = list2_number*10 + link_list2.get_value(i)

    sum_number = list1_number + list2_number
    sum_list = LinkedList()
    while sum_number>0:
        sum_list.append(sum_number%10)
        sum_number//= 10
    
    return sum_list
def intersection(self,link_list1:LinkedList,link_list2:LinkedList)->LinkedList:
    pass
    # return
def partition(link_list:LinkedList,value):
    last_search_index = -1
    for i in range(link_list.length,-1,-1):
        if link_list.get_value(i) == value:
            last_search_index = i
            break

    stop = last_search_index -1
    runtime = 0
    
    while stop>runtime:
        if link_list.get_value(runtime) >= value and link_list.get_value(stop)<value:
            link_list.swap_value(runtime,stop)
            runtime += 1
            stop -= 1
        elif link_list.get_value(runtime) >= value and link_list.get_value(stop)>=value:
            stop -= 1
        elif link_list.get_value(runtime) < value and link_list.get_value(stop)<value:
            runtime += 1
        else:
            runtime += 1

    if last_search_index == -1:
        return False



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
    new_linked_list.insert(1,11)
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
    new_linked_list.reserve()
    i = 10
    
    new_linked_list.traversal()
    print(f'Phần tử thứ {i} từ giá trị cuối cùng của linked list là: {new_linked_list.find_nth_to_last_element(i)}')

    # new_linked_list.remove(7)

    # print(new_linked_list.get(8))
    # new_linked_list.traversal()
    # print(new_linked_list.head.value)
    # print(new_linked_list.tail.value)
    # print('ddo dang',new_linked_list.length)

    ll1 = LinkedList()
    ll1.append([7,1,6])

    ll2 = LinkedList()
    ll2.append([5,9,2])

    sum_ll = sum_list(ll1,ll2)
    sum_ll.traversal()

    ll3 = LinkedList()
    # ll3.append([11,3,9,10,15])
    ll3.append([11,3,9,10,15,11,21,3,9])
    ll3.remove_duplicates()
    ll3.traversal()
    ll3.remove_linked_list_element(11)
    # partition(ll3,10)
    ll3.traversal()
    # remove_duplicates_by_head(ll3.head)
    ll3.traversal()
    # print(remove_linked_list_element_by_head(ll3.head,3))