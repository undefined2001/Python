class Node:
  def __init__(self, e, n):
    self.element = e
    self.next = n


class LinkedList:
  
  def __init__(self, a):
    if type(a) == list:
          self.head = Node(a[0], None)
          tail = self.head
          i = 1
          while i < len(a):
              newNode = Node(a[i], None)
              tail.next = newNode
              tail = newNode
              i += 1
    else:
        self.head = a
        tail = self.head
        temp = a
        while temp != None:
            tail.next = temp.next
            tail = temp.next
            temp = temp.next
    
  # Count the number of nodes in the list
  def countNode(self):
    count = 0
    temp = self.head
    while temp != None:
        count += 1
        temp = temp.next
    return count
  # Print elements in the list
  def printList(self):
    temp = self.head
    while temp != None:
        print(temp.element, end = ", " if (temp.next != None) else "" )
        temp = temp.next
    print()

  # returns the reference of the Node at the given index. For invalid index return None.
  def nodeAt(self, idx):
    if (idx < 0 or idx >= self.countNode()):
        print("Invalid Index")
    else:
        temp = self.head
        i = 0
        while temp != None:
            if (i == idx):
                return temp 
            i += 1
            temp = temp.next
  
  # returns the element of the Node at the given index. For invalid idx return None.
  def get(self, idx):
    if (idx < 0 or idx >= self.countNode()):
        return None
    else:
        temp = self.head
        i = 0
        while temp != None:
            if (i == idx):
                return temp.element 
            i += 1
            temp = temp.next
  # updates the element of the Node at the given index. 
  # Returns the old element that was replaced. For invalid index return None.
  # parameter: index, element
  def set(self, idx, elem):
    replaced_value = 0
    if (idx < 0 or idx >= self.countNode()):
        return None
    else:
        temp = self.head
        i = 0
        while temp != None:
            if (i == idx):
                replaced_value = temp.element
                temp.element = elem 
                return replaced_value
            i += 1
            temp = temp.next

  # returns the index of the Node containing the given element.
  # if the element does not exist in the List, return -1.
  def indexOf(self, elem):
    flag = False
    temp = self.head
    i = 0
    while temp != None:
        if (temp.element == elem):
            return_value = i
            flag = True
            break;
        temp = temp.next
        i += 1
    return return_value if (flag) else -1
  
  # returns true if the element exists in the List, return false otherwise.
  def contains(self, elem):
    flag = False
    temp = self.head
    i = 0
    while temp != None:
        if (temp.element == elem):
            return_value = i
            flag = True
            break;
        temp = temp.next
        i += 1
    return flag

  # Makes a duplicate copy of the given List. Returns the reference of the duplicate list.
  def copyList(self):
        copy_list = Node(self.head.element, None)
        tail = copy_list
        temp = self.head
        while temp != None:
            tail.next = temp.next
            tail = temp.next
            temp = temp.next
        
        return copy_list
    

  # Makes a reversed copy of the given List. Returns the head reference of the reversed list.
  def reverseList(self):
    copy_list = Node((self.nodeAt(self.countNode()-1)).element, None)
    tail = copy_list
    for i in range(self.countNode()-2, -1, -1):
        newNode = Node(self.nodeAt(i).element, None)
        tail.next = newNode
        tail = newNode
    return copy_list

  
  # inserts Node containing the given element at the given index
  # Check validity of index.
  def insert(self, elem, idx):
    if idx <0 or idx > self.countNode():
      print("Invalid Index")
    elif idx == 0:
      newNode= Node(elem, None)
      newNode.next=self.head
      self.head = newNode
      return
    else:
      newNode = Node(elem, None)
      predNode= self.nodeAt(idx-1)
      newNode.next= predNode.next
      predNode.next=newNode
      return


  # removes Node at the given index. returns element of the removed node.
  # Check validity of index. return None if index is invalid.
  def remove(self, idx):
    rem_val = 0
    if (idx < 0 or idx >= self.countNode()):
        return None
    else:
        if idx == 0:
            rem_node = self.head
            self.head = self.head.next
            rem_val = rem_node.element
            rem_node.element = None
            rem_node.next = None
        else:
            prev = self.nodeAt(idx-1)
            rem_node = prev.next
            prev.next = rem_node.next
            rem_val = rem_node.element
            rem_node.next = None
            rem_node.element = None
        return rem_val
  
  # Rotates the list to the left by 1 position.
  def rotateLeft(self):
    temp = self.head
    last_node = self.nodeAt(self.countNode()-1)
    self.head = self.head.next
    last_node.next = temp 
    temp.next = None
  
  
  # Rotates the list to the right by 1 position.
  def rotateRight(self):
    last_prev_node = self.nodeAt(self.countNode()-2)
    temp = self.head
    self.head = last_prev_node.next
    self.head.next = temp 
    last_prev_node.next = None