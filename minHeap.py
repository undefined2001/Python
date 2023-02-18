class MinHeap:
    def __init__(self, capacity):
        self.size = 0
        self.capacity = capacity
        self.arr = [0] * (self.capacity + 1)

    # This is the section of utility Function

    # returns parent index of an index
    def parent(self, index: int) -> int:
        return (index) // 2

    # returns left child of an index
    def left_child(self, index: int) -> int:
        return 2 * index

    # returns right child of an index
    def right_child(self, index: int) -> int:
        return 2 * index + 1

    # it helps to bring a value from the last index to it's position after insertion / add

    def swim(self, i):
        while i > 0 and self.arr[self.parent(i)] > self.arr[i]:
            self.arr[self.parent(
                i)], self.arr[i] = self.arr[i], self.arr[self.parent(i)]
            i = self.parent(i)

    # it helps a value to go down when it is swaped while deletion
    def sink(self, i):
        # this loop will continue until it reaches a leaf or an index with no child
        while self.left_child(i) <= self.size:
            smaller_child = self.left_child(i)

            # comparing two children to take the smaller one for comparing with parent
            if self.right_child(i) <= self.size and self.arr[self.right_child(i)] < self.arr[smaller_child]:
                smaller_child = self.right_child(i)

            # comparing smaller child with the parent
            if self.arr[smaller_child] < self.arr[i]:
                self.arr[i], self.arr[smaller_child] = self.arr[smaller_child], self.arr[i]
                i = smaller_child

            # if the order of the min heap is already correct it will break
            else:
                break

    # End Utility Function's Section

    # this helps to insert a element in the heap
    def add(self, val: int) -> int:
        if self.size == self.capacity:
            print('Heap is full')
            return
        self.size += 1
        self.arr[self.size] = val
        self.swim(self.size)
        return val

    # it helps to build a heap from an array

    def build(self, arr):
        for i in arr:
            self.add(i)

    # it deletes the smallest(root) value from the min heap

    def delete(self) -> int:
        delete_val = self.arr[1]
        self.arr[1], self.arr[self.size] = self.arr[self.size], self.arr[1]
        self.size -= 1
        self.arr[self.size+1] = 0
        self.sink(1)
        return delete_val

    # this return a sorted array in ascending order
    def heapsort(self):
        temp = [0] * self.size
        i = 0
        while self.size > 0:
            temp[i] = self.delete()
            i += 1
        return temp


heap = MinHeap(50)
while True:
    print("1. Enter 'A' to Add")
    print("2. Enter 'B' to Delete")
    print("3. Enter 'S' to Sort")
    print("4. Enter 'Q' to quit")
    inp = input("Enter Your Command -> ")
    if inp == "A":
        a = heap.add(int(input("Enter the value you want to Add: ")))
        print(a, "Added Successfully")

    elif inp == "B":
        b = heap.delete()
        print(b, "Deleted Successfully")

    elif inp == "S":
        arr = heap.heapsort()
        print("Here is Your Sorted List:", arr)
    elif inp == "Q":
        print("Exited")
        break
