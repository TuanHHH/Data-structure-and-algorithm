class Node:

  def __init__(self, value) -> None:
    self.value = value
    self.next = None


class LinkedList:

  def __init__(self) -> None:
    self.head = None
    self.tail = None
    self.length = 0

  def append(self, value):
    if isinstance(value, list) is True:
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

  def reserve(self):
    current_node = self.head
    prev_node = None
    while current_node:
      next_node = current_node.next
      current_node.next = prev_node
      prev_node = current_node
      current_node = next_node
    self.head, self.tail = self.tail, self.head

  def traversal(self):
    temp = 'Linked list:'
    current_node = self.head
    while current_node:
      temp += f'{current_node.value}->'
      current_node = current_node.next
    print(temp.rstrip('->'))

  def get_value(self, index):
    if index < 0 or index >= self.length:
      return False
    current = self.head
    for _ in range(0, index):
      current = current.next
    return current.value


def sum_list(link_list1: LinkedList, link_list2: LinkedList) -> LinkedList:
  link_list1.reserve()
  link_list2.reserve()
  list1_number = 0
  for i in range(link_list1.length):
    list1_number = list1_number * 10 + link_list1.get_value(i)
  list2_number = 0
  for i in range(link_list2.length):
    list2_number = list2_number * 10 + link_list2.get_value(i)

  sum_number = list1_number + list2_number
  sum_list = LinkedList()
  while sum_number > 0:
    sum_list.append(sum_number % 10)
    sum_number //= 10
  return sum_list


ll1 = LinkedList()
ll1.append([7, 1, 6])
ll2 = LinkedList()
ll2.append([5, 9, 2])
sum_list = sum_list(ll1, ll2)
sum_list.traversal()