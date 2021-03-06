class Stack:

  def __init__(self):
    self.items = []

  def is_empty(self):
    return self.items == []

  def push(self, item):
    self.items.append(item)

  def pop(self):
    return self.items.pop()

  def peek(self):
    return self.items[len(self.items)-1]


class Queue:

  def __init__(self):
    self.items = []

  def is_empty(self):
    return self.items == []

  def enqueue(self, item):
    self.items.insert(0, item)

  def dequeue(self):
    return self.items.pop()

  def size(self):
    return len(self.items)


class Deque():

  __init__(self):
    self.items = []

  def is_empty(self):
    return self.items == []

  def add_front(self, item):
    self.items.append(item)

  def add_rear(self, item):
    self.items.insert(0, item)

  def remove_front(self):
    return self.items.pop()

  def remove_rear(self):
    return self.items.pop(0)

  def size(self):
    return len(self.items)


class Node:

  def __init__(self, init_data):
    self.data = init_data
    self.next = None

  def get_data(self):
    return self.data

  def get_next(self):
    return self.next

  def set_data(self, new_data):
    self.data = new_data

  def set_next(self, new_next):
    self.next = new_next


class UnorderedList:

  def __init__(self):
    self.head = None

  def is_empty(self):
    return self.head == None

  def add(self, item):
    temp = Node(item)
    temp.set_next(self.head)
    self.head = temp

  def size(self):
    current = self.head
    count = 0
    while current != None:
      current = current.get_next()
      count = count + 1
    return count

  def search(self, item):
    current = self.head
    found = False
    while current != None and not found:
      if current.get_data() == item:
        found = True
      else:
        current = current.get_next()
    return found

  def remove(self, item):
    current = self.head
    previous = None
    found = False
    while current != None and not found:
      if current.get_data == item:
        found = True
      else:
        previous = current
        current = current.get_next()
    if previous == None:
      self.head = current.get_next()
    else:
      previous.set_next(current.get_next())

  # append() with O(n) efficiency
  def append(self, item):
    current = self.head
    temp = Node(item)
    while current != None:
      current = current.get_next()
    current.set_next(temp)


class OrderedList:

  def __init__(self):
    self.head = None

  def is_empty(self):
    return self.head == None

  def add(self, item):
    current = self.head
    previous = None
    stop = False
    while current != None and not stop:
      if current.get_data() > item:
        stop = True
      else:
        previous = current
        current = current.get_next()
    temp = Node(item)
    if previous = None:
      temp.set_next(self.head)
      self.head = temp
    else:
      temp.set_next(current)
      previous.set_next(temp)

  def size(self):
    current = self.head
    count = 0
    while current != None:
      current = current.get_next()
      count = count + 1
    return count

  def search(self, item):
    current = self.head
    found = False
    stop = False
    while current != None and not found and not stop:
      if current.get_data() == item:
        found = True
      else:
        if current.get_data() > item:
          stop = True
        else:
          current = current.get_next()
    return found

  def remove(self, item):
    current = self.head
    previous = None
    found = False
    while current != None and not found:
      if current.get_data == item:
        found = True
      else:
        previous = current
        current = current.get_next()
    if previous == None:
      self.head = current.get_next()
    else:
      previous.set_next(current.get_next())

  # append() with O(n) efficiency
  def append(self, item):
    current = self.head
    temp = Node(item)
    while current != None:
      current = current.get_next()
    current.set_next(temp)

