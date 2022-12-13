class KeyIndexSorting:
  def __init__(self, arr):
    self.max = 0
    for i in arr:
      if self.max < i:
        self.max = i
    self.k = [0]*(self.max * 2 +1)
    # print(len(self.k), self.max)
    for i in range(len(arr)):
      self.k[arr[i]+self.max] += 1


  def keyindexsearch(self, val):
      if self.k[val + self.max] != 0:
        return True
      else:
        return False

  def sorting(self):
    count = 0
    for i in range(len(self.k)):
      if self.k[i] != 0:
        count += self.k[i]

    newarr = [0] * count   
    j = 0
    for i in range(len(self.k)):
      if self.k[i] > 0:
        newarr[j] = i-self.max
        j += 1
    return newarr

arr = [-10, -5, 5, 10, 3]

obj = KeyIndexSorting(arr)
print(obj.keyindexsearch(-5))
print(obj.sorting())
  

