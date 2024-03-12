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

  def find_nth_to_last_element(self, index: int):
    if index < 1 or index > self.length:
      return False
    else:
      current_node = self.head
      for _ in range(self.length - index):
        current_node = current_node.next
    return current_node.value


ll1 = LinkedList()
ll1.append([1, 2, 0, 3, 5])
print(ll1.find_nth_to_last_element(2))
