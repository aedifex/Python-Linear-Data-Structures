import random

class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    
  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list
  
  def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      while current_node:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.set_next_node(next_node.get_next_node())
          current_node = None
        else:
          current_node = next_node

  def insert_end(self, new_value):
    new_node = Node(new_value)
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_next_node() == None:
        print(current_node.get_value())
        print("End of list!")
      current_node = current_node.get_next_node()
      new_node.set_next_node(current_node)

  def arrayify(self):
    a = []
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        a.append(current_node.get_value())
      current_node = current_node.get_next_node()
    return a

  def get_length(self):
    l = 0
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        l += 1
      current_node = current_node.get_next_node()
    return l

# init list
myList = LinkedList(random.randint(0, 100))

# populate list of N length with M values
for n in range(9):
  myList.insert_beginning(random.randint(0, 100))

# print(myList.stringify_list())
print(myList.arrayify())

print(myList.get_length())

print(myList.arrayify())
