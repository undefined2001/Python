class CircularArray:
  def __init__(self, lin, st, sz):
    if st < 0 or sz < 0:
        print("Invalid Input")
    else:
        self.start = st
        self.size = sz
        self.cir = [None]*len(lin)
        cirIndex = self.start
        linIndex = 0
        while linIndex < self.size:
            self.cir[cirIndex % len(self.cir)] = lin[linIndex]
            cirIndex = cirIndex + 1 
            linIndex += 1


    


    
    # if lin = [10, 20, 30, 40, None]
    # then, CircularArray(lin, 2, 4) will generate
    # cir = [40, null, 10, 20, 30]
    
    # To Do. 
    # Hints: set the values for initialized variables
  
  # Print from index 0 to len(cir) - 1
  def printFullLinear(self): #Easy
    index = 0
    while index < len(self.cir):
      print(self.cir[index ], end = " ")
      index += 1
    print()

  
  # Print from start index and total size elements
  def printForward(self): #Easy
    index = self.start
    while index < self.size + self.start:
      print(self.cir[index % len(self.cir)], end = " ")
      index += 1
    print()
  
  def printBackward(self): #Easy
    index = ((self.start + self.size-1) % len(self.cir))
    print(self.start, self.size, index, len(self.cir))
    loopcontroller = 0
    while loopcontroller < self.size:
      if index < 0:
        index = len(self.cir) - 1
        print(index)
      print(self.cir[index], end = " ")
      index -= 1
      loopcontroller += 1
    print()
  # With no null cells
  def linearize(self): #Medium
    index = 0
    count = 0
    while index < len(self.cir):
        if self.cir[index] == None:
            count += 1
        index += 1

    newarr = [0] * (len(self.cir)-count)
    idx = self.start
    while idx < self.size + self.start:
        newarr[idx-self.start] = self.cir[idx % len(self.cir)]
        idx += 1
    
    self.cir = newarr

  
  # Do not change the Start index
  def resizeStartUnchanged(self, newcapacity): #Medium
    newarr = [None] * newcapacity
    index = 0 
    while index < self.size:
      newarr[(index + self.start) % len(newarr)] = self.cir[(index+self.start) % len(self.cir)]
      index += 1

    self.cir = newarr
  
  # This method will check whether the array is palindrome or not
  def palindromeCheck(self): #Hard
    start = self.start 
    end = (self.size+self.start) % len(self.cir) -1
    mid = (self.size+self.start)/2 + 1
    index = 0
    flag = True
    while index < mid:
      if end < 0:
        end = len(self.cir) -1
      if self.cir[(index + start) % len(self.cir)] == self.cir[end]:
        flag = True
      else:
        flag = False
        break;
      index += 1
      end -= 1
    if flag == True:
      print("This array is a palindrom")
    else:
      print("This array is not a palindrom")

  # This method will sort the values by keeping the start unchanged
  # def sort(self):
  #   start = self.start 
  #   end = (self.size+self.start) % len(self.cir) -1
  #   index = 0
  #   flag = True
  #   for i in range(self.size):
  #     for j in range(i+1, self.size):
  #       if self.cir[(i + start) % len(self.cir)] > self.cir[(j+start) % len(self.cir)]:
  #         temp = self.cir[(i + start) % len(self.cir)]
  #         self.cir[(i + start) % len(self.cir)] = self.cir[(j+start) % len(self.cir)]
  #         self.cir[(j+start) % len(self.cir)] = temp
  

  def sort(self):
    # To Do
    index = self.start
    n = 0
    while(n < self.size):
        min_idx = index
        for i in range(n+self.start ,self.size+self.start-1):
            i = (i+1) % len(self.cir)
            hold_1 = self.cir[i]
            #hold_1 = self.cir[i]
            #print(type(hold_1))
            hold_2 = self.cir[min_idx]
            # print(hold_1, hold_2)
            if(hold_1 < hold_2):
                min_idx = i
                
        temp = self.cir[min_idx]
        self.cir[min_idx] = self.cir[index]
        self.cir[index] = temp
        
        index = (index+1) % len(self.cir)
        
        n += 1
  # This method will check the given array across the base array and if they are equivalent interms of values return true, or else return false
  def equivalent(self, cir_arr):
    start_one = self.start
    start_two = cir_arr.start
    flag = True
    if self.size == cir_arr.size:
      index = 0
      while index < self.size:
        if self.cir[(start_one + index) % len(self.cir)] == cir_arr.cir[(start_two + index) % len(cir_arr.cir)]:
          flag = True
        else:
          flag = False
          break;
        index += 1
    else:
      flag = False
    return flag



  # the method take another circular array and returns a linear array containing the common elements between the two circular arrays.
  def intersection(self, c2):
    newstring = ""
    index = 0
    #taking start and size for self
    start_one = self.start
    size_one= self.size
    #taking start and size for c2
    size_two = c2.size
    #looping size times
    while index < size_one:
      j = 0
      start_two = c2.start
      #chacking if any item is equal to self.cir[start]
      while j < size_two:
        if self.cir[start_one] == c2.cir[start_two]:
          newstring += (str(self.cir[start_one])+", ")
        start_two = (start_two + 1) % len(c2.cir)
        j+=1
      index += 1
      start_one = (start_one + 1) % len(self.cir)
    #for formatting the output list
    newArr = [0] * (len(newstring.split(", "))-1)
    for i in range(len(newstring.split(", "))-1):
      newArr[i] = int(newstring.split(", ")[i])
    return newArr


#Testing Starts from Here

# Tester class. Run this cell after completing methods in the upper cell and
# check the output

lin_arr1 = [10, 20, 30, 40, None]

print("==========Test 1==========")
c1 = CircularArray(lin_arr1, 2, 4)
c1.printFullLinear() # This should print: 40, None, 10, 20, 30
c1.printForward() # This should print: 10, 20, 30, 40
c1.printBackward() # This should print: 40, 30, 20, 10

print("==========Test 2==========")
c1.linearize()
c1.printFullLinear() # This should print: 10, 20, 30, 40

print("==========Test 3==========")
lin_arr2 = [10, 20, 30, 40, 50]
c2 = CircularArray(lin_arr2, 2, 5)
c2.printFullLinear() # This should print: 40, 50, 10, 20, 30
c2.resizeStartUnchanged(8) # parameter --> new Capacity
c2.printFullLinear() # This should print: None, None, 10, 20, 30, 40, 50, None

print("==========Test 4==========")
lin_arr3 = [10, 20, 30, 20, 10, None, None]
c3 = CircularArray(lin_arr3, 3, 5)
c3.printForward() # This should print: 10, 20, 30, 20, 10
c3.palindromeCheck() # This should print: This array is a palindrome

print("==========Test 5==========")
lin_arr4 = [10, 20, 30, 20, None, None, None]
c4 = CircularArray(lin_arr4, 3, 4)
c4.printForward() # This should print: 10, 20, 30, 20
c4.palindromeCheck() # This should print: This array is NOT a palindrome

print("==========Test 6==========")
lin_arr5 = [10, 20, -30, 20, 50, 30, None]
c5 = CircularArray(lin_arr5, 5, 6)
c5.printForward() # This should print: 10, 20, -30, 20, 50, 30
c5.sort()
c5.printForward() # This should print: -30, 10, 20, 20, 30, 50

print("==========Test 7==========")
lin_arr6 = [10, 20, -30, 20, 50, 30, None]
c6 = CircularArray(lin_arr6, 2, 6)
c7 = CircularArray(lin_arr6, 5, 6)
c6.printForward() # This should print: 10, 20, -30, 20, 50, 30
c7.printForward() # This should print: 10, 20, -30, 20, 50, 30
print(c6.equivalent(c7)) # This should print: True

print("==========Test 8==========")
lin_arr7 = [10, 20, -30, 20, 50, 30, None, None, None]
c8 = CircularArray(lin_arr7, 8, 6)
c6.printForward() # This should print: 10, 20, -30, 20, 50, 30
c8.printForward() # This should print: 10, 20, -30, 20, 50, 30
print(c6.equivalent(c8)) # This should print: True

print("==========Test 9==========")
lin_arr8 = [10, 20, 30, 40, 50, 60, None, None, None]
c9 = CircularArray(lin_arr8, 8, 6)
c6.printForward() # This should print: 10, 20, -30, 20, 50, 30
c9.printForward() # This should print: 10, 20, 30, 40, 50, 60
print(c6.equivalent(c9)) # This should print: False

print("==========Test 10==========")
lin_arr9 = [10, 20, 30, 40, 50, None, None, None]
c10 = CircularArray(lin_arr9, 5, 5)
c10.printFullLinear() # This should print: 40, 50, None, None, None, 10, 20, 30
lin_arr10 = [5, 40, 15, 25, 10, 20, 5, None, None, None, None, None]
c11 = CircularArray(lin_arr10, 8, 7)
c11.printFullLinear() # This should print: 10, 20, 5, None, None, None, None, None, 5, 40, 15, 25
output = c10.intersection(c11)
print(output) # This should print: [10, 20, 40]
