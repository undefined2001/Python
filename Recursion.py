 #Task 1-A
def fact(n):
    return 1 if n == 0 else n * fact(n-1)
print(fact(4))

#Task 1-B

def fib(nth):
    if nth == 0 or nth == 1:
        return nth
    return fib(nth-1) + fib(nth-2)
    print(nth)
fib(10)

#Task 1-C

def printArray(arr, i = 0):
    if i == len(arr):
        return
    print(arr[i])
    printArray(arr, i+1)

a = [1, 2, 3, 4, 5]
printArray(a)

# Task 1-D
def square(base, n):
    if n == 0:
        return 1
    return base * square(base, n-1)
print(square(3, 2))

#Task 2-A
def binaryConverter( num ):
	return 0 if num == 0 else num % 2 + 10 * binaryConverter(int(num // 2))
num = int(input())
print(binaryConverter(num))


#Task 2-B
class Node:
    def __init__(self, e):
        self.elem = e
        self.next = None

n1 = Node(5)
n2 = Node(10)
n3 = Node(15)
n1.next = n2
n2.next = n3

def addNode(temp):
    if temp == None:
        return 0
    return temp.elem + addNode(temp.next)

print(addNode(n1))

# Task 2-C
class Node:
    def __init__(self, e):
        self.elem = e
        self.next = None

n1 = Node(5)
n2 = Node(10)
n3 = Node(15)
n1.next = n2
n2.next = n3


def printLinkedListReverse(temp):
    if temp == None:
        return
    printLinkedListReverse(temp.next)
    print(temp.elem)

printLinkedListReverse(n1)

#Task-3

def hocBuilder(height):
    if height == 0:
        return
    elif height == 1:
        return 8
    return 5 + hocBuilder(height-1)

print(hocBuilder(3))

# Task 4-A
def patternprint(n):
    if n == 0:
        return
    patternprint(n-1)
    print( n, end = " ")

def patterncontrol(n):
    if n == 0:
        return
    patterncontrol(n-1)
    patternprint(n)
    print()
n = int(input("Enter a Number: "))
patterncontrol(n)

#Task 4-B

def spaceprint(n, a):
    if n == a:
        return
    spaceprint(n, a-1)
    print(" ", end = " ")

def patternprint(n):
    if n == 0:
        return
    patternprint(n-1)
    print(n, end = " ")

def patterncontrol(n, a):
    if n == 0:
        return
    patterncontrol(n-1, a)
    spaceprint(n-1, a)
    print("", end = "")
    patternprint(n)
    print()
n = int(input("Enter a Number: "))
patterncontrol(n, n-1)

#Task 5
class FinalQ:
    def print(self,array,idx):
        if(len(array) > idx):
            profit = float(self.calcProfit(array[idx]))
            print(f"{idx+1}. Investment: {array[idx]}; Profit: {profit}")
            self.print(array,idx+1)
        else:
            return

    def calcProfit(self,invest):
        if invest == 25000:
            return 0
        elif invest <= 100000:
            return (225 + self.calcProfit(invest-5000))
        elif 100000 < invest:
            return (400 + self.calcProfit(invest-5000))


array=[25000,100000,250000,350000]
f = FinalQ()
f.print(array,0)
