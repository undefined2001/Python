class ArrayStack:
  def __init__(self, len = 10):
    self.arr = [0]*len
    self.size = 0

  def push(self, val):
    if self.size == len(self.arr):
      print("Stack Overflow")

    else:
      self.arr[self.size] = val
      self.size += 1
      return val
  
  def pop(self):
    if self.size > 0:
      rem = self.arr[self.size - 1]
      self.size -= 1
      return rem
    else:
      print("Stack Underflow")

  def peek(self):
    return self.arr[self.size-1]


testString = "1+2*[3*3+{4–5}(6(7/8/9)+10)–11+(12*8)]+14"
stack1 = ArrayStack(len(testString))
opening = "({["
closing = ")}]"


#function to check Error

def expressionChecker(testString, stack1):
  flag = False
  for i in range(len(testString)):
    if testString[i] == opening[2] or testString[i] == opening[1] or testString[i] == opening[0]:
      stack1.push(testString[i])
    elif testString[i] == closing[0] or testString[i] == closing[1] or testString[i] == closing[2]:
      popval = stack1.pop()
      if popval == opening[0] and testString[i] == closing[0]:
        flag = True
      elif popval == opening[1] and testString[i] == closing[1]:
        flag = True
      elif popval == opening[2] and testString[i] == closing[2]:
        flag = True
      else:
        count = 0
        if popval == opening[2] or popval == opening[1] or popval == opening[0]:
          for i in range(len(testString)):
            if popval == testString[i]:
              count = i+1
          print(f"Error at character # {count}. ‘{popval}‘- not closed.")
          flag = False
        else:
          print(f"Error at character # {count}. ‘{popval}‘- has no opening.")
          flag = False
        break

  if flag:
    print("This Expression is correct")

expressionChecker(testString, stack1)

    

#LinkedList part starts here


class Node:
  def __init__(self, value = 0, next = 0):
    self.elem = value
    self.next = next
class LinkedListStack:
  def __init__(self):
    self.head = None
    self.size = 0
    

  def push(self, val):
    if self.head == None:
      self.head = Node(val)
      self.size = 1
    else:
      newNode = Node(val)
      newNode.next = self.head
      self.head = newNode
      self.size += 1
      return val
  
  def pop(self):
    if self.head == None:
      print("Stack Underflow")
    else:
      rm = self.head.elem
      self.head = self.head.next
      self.size -= 1
      return rm

  def peek(self):
    return self.head.elem

testString = "1+2*[3*3+{4-5(6(7/8/9)+10)-11+(12*8)]+14"
stack = LinkedListStack()
expressionChecker(testString, stack)

