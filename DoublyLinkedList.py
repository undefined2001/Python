class Node:
  def __init__(self, elem):
    self.element = elem
    self.next = None
    self.prev = None


class DoublyList:
  
  def __init__(self, a):
    self.head = Node(a[0])
    tail = self.head
    if type(a) == list:
      for i in range(1, len(a)):
        newNode = Node(a[i])
        newNode.prev = tail
        tail.next = newNode
        tail = newNode
    else:
      pass

  
  # Counts the number of Nodes in the list
  def countNode(self):
    temp = self.head
    count = 0
    while temp != None:
      count += 1
      temp = temp.next
    return count
  
  # prints the elements in the list
  def forwardprint(self):
    temp = self.head
    while temp != None:
      print(temp.element, end = ", " if (temp.next != None) else "\n" )
      temp = temp.next

  # prints the elements in the list backward
  def backwardprint(self):
    temp = self.head
    while temp.next != None:
      temp = temp.next
    while temp != None:
      print(temp.element, end = ", " if (temp.prev != None) else "\n" )
      temp = temp.prev
  # returns the reference of the at the given index. For invalid index return None.
  def nodeAt(self, idx):
    if (idx < 0 or idx >= self.countNode()):
        return None
    else:
        temp = self.head
        i = 0
        while temp != None:
            if (i == idx):
                return temp
            i += 1
            temp = temp.next
  
  # returns the index of the containing the given element. if the element does not exist in the List, return -1.
  def indexOf(self, elem):
    temp = self.head
    count = 0
    while temp != None:
      if temp.element == elem:
        return count
      else:
        count += 1
      temp = temp.next

  # inserts containing the given element at the given index Check validity of index. 
  def insert(self, elem, idx):
    if idx < 0 or idx > self.countNode():
      print("Invalid Index")
    elif idx == 0:
      newNode= Node(elem, None, None)
      newNode.next = self.head
      self.head.prev = newNode
      self.head = newNode
      return
    elif idx == self.countNode():
      newNode = Node(elem)
      predNode = self.nodeAt(idx-1)
      newNode.prev = predNode
      predNode.next = newNode

    else:
      newNode = Node(elem)
      predNode = self.nodeAt(idx-1)

      nextNode = predNode.next

      newNode.next = predNode.next
      newNode.prev = predNode
      predNode.next.prev = newNode
      predNode.next = newNode

     

      return

  # removes at the given index. returns element of the removed node. Check validity of index. return None if index is invalid.
  def remove(self, idx):
    if idx == 0:
      rn = self.head
      nextNode = self.head.next
      self.head = nextNode
      nextNode.prev = None
      return str(rn.element)
    elif idx == self.countNode()-1:
      removeNode = self.nodeAt(idx)
      re = removeNode.element
      prev = removeNode.prev
      prev.next = None
      return str(re)
    else:
      removeNode = self.nodeAt(idx)
      re = removeNode.element
      prev = removeNode.prev
      nextNode = removeNode.next
      prev.next = nextNode
      nextNode.prev = prev
      removeNode.element = removeNode.prev = removeNode.next = None
      return str(re)
      
arr = [1, 4, 2]
newlist = DoublyList(arr)
newlist.insert(20,1)
newlist.remove(1)
newlist.forwardprint()
