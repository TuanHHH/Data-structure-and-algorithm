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

  def get_value(self, index):
    if index < 0 or index >= self.length:
      return False
    current = self.head
    for _ in range(0, index):
      current = current.next
    return current.value

  def get(self, index):
    if index < 0 or index >= self.length:
      return False
    current = self.head
    for _ in range(0, index):
      current = current.next
    return current

  def swap_value(self, index1: int, index2: int):
    if index1 < 0 or index2 < 0 or index1 >= self.length or index2 >= self.length:
      return False
    elif index1 == index2:
      return
    else:
      if index1 > index2:
        index1, index2 = index2, index1

      if index1 == 0 and index2 == self.length - 1:
        before_node2 = self.get(index2 - 1)
        before_node2.next = self.head
        self.head.next, self.tail.next = self.tail.next, self.head.next
        self.head, self.tail = self.tail, self.head

      elif index1 == 0:
        node2 = self.get(index2)
        before_node2 = self.get(index2 - 1)

        f_node = self.head
        before_node2.next = f_node

        f_node.next, node2.next = node2.next, f_node.next
        self.head = node2

      elif index2 == self.length - 1:
        node1 = self.get(index1)
        node2 = self.tail
        before_node1 = self.get(index1 - 1)
        before_node2 = self.get(index2 - 1)

        before_node1.next, before_node2.next = before_node2.next, before_node1.next

        node2.next = node1.next

        self.tail = node1
        self.tail.next = None

      else:
        node1 = self.get(index1)
        node2 = self.get(index2)
        before_node1 = self.get(index1 - 1)
        before_node2 = self.get(index2 - 1)
        before_node1.next, before_node2.next = before_node2.next, before_node1.next
        node1.next, node2.next = node2.next, node1.next

  def traversal(self):
    temp = 'Linked list:'
    current_node = self.head
    while current_node:
      temp += f'{current_node.value}->'
      current_node = current_node.next
    print(temp.rstrip('->'))


def partition(link_list: LinkedList, value):
  last_search_index = -1
  for i in range(link_list.length, -1, -1):
    if link_list.get_value(i) == value:
      last_search_index = i
      break

  stop = last_search_index - 1
  runtime = 0

  while stop > runtime:
    if link_list.get_value(runtime) >= value and link_list.get_value(
        stop) < value:
      link_list.swap_value(runtime, stop)
      runtime += 1
      stop -= 1
    elif link_list.get_value(runtime) >= value and link_list.get_value(
        stop) >= value:
      stop -= 1
    elif link_list.get_value(runtime) < value and link_list.get_value(
        stop) < value:
      runtime += 1
    else:
      runtime += 1

  if last_search_index == -1:
    return False


ll = LinkedList()
ll.append([11, 3, 9, 10, 15])
partition(ll, 10)
ll.traversal()
