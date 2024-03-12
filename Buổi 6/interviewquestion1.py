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

  def remove_duplicates(self):
    if self.head == None:
      return
    else:
      current_node = self.head
      node_values = set()
      node_values.add(current_node.value)
      while current_node.next:
        if current_node.next.value in node_values:
          current_node.next = current_node.next.next
          self.length -= 1
        else:
          node_values.add(current_node.next.value)
          current_node = current_node.next
      self.tail = current_node

  def traversal(self):
    temp = 'Linked list:'
    current_node = self.head
    while current_node:
      temp += f'{current_node.value}->'
      current_node = current_node.next
    print(temp.rstrip('->'))


ll = LinkedList()
ll.append([1, 1, 2, 2, 3, 4, 4, 5])
ll.remove_duplicates()
ll.traversal()
