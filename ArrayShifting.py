#Task-1
#LeftShift
source = [10,20,30,40,50,60,70]
def leftShift(arr, k):
    if k < 0:
        return "Invalid Value"
    else:
        for i in range(len(arr)):
            if i < len(arr)-k:
                arr[i] = arr[i+k]
            else:
                arr[i] = 0
        return arr
source = leftShift(source,6)
print(source)


#Task-2
#LeftRotation
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr
def leftRotation(arr, k):
    if k < 0:
        return "Invalid Value"
    else:
        k %= len(arr)
        reverse(arr, 0, len(arr)-1)
        reverse(arr, len(arr)-k, len(arr)-1)
        reverse(arr, 0, len(arr)-k-1)
        return arr

a = [10,20,30,40,50,60]
a = leftRotation(a, 2)
print(a)



#Task-3
#RightShift
source=[10,20,30,40,50,60]
def rightShift(arr, k):
    if k < 0:
        return "Invalid Value"
    else:
        for i in range(len(arr)-1,-1,-1):
            arr[i] = arr[i-k]
            if i < k:
                arr[i] = 0
        return arr
source = rightShift(source,3)
print(source)



#Task-4
#RightRotation
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr
def rightRotation(arr, k):
    if k < 0:
        return "Invalid Value"
    else:
        k %= len(arr)
        reverse(arr, 0, len(arr)-k-1)
        reverse(arr, len(arr)-k, len(arr)-1)
        reverse(arr, 0, len(arr)-1)
        return arr
a = [10,20,30,40,50,60]
a = rightRotation(a, 2)
print(a)


# Task-5 
#Removing element at a index
def remove(arr, size, index):
    if index < size:
        idx = 0
        while idx < size-1:
            if idx >= index:
                arr[idx] = arr[idx+1]
            idx += 1
        arr[size-1] = 0 
        return arr
    
source=[10,20,30,40,50]
source = remove(source, 5, 2)
print(source)


#Task-6
#RemoveDuplicates
# source = [10,2,2,30,2,50,2,2,0,0]
source = [10,2,2,30,2,30,50,2,2,2,0,0]
def removeDuplicate(arr, size, element):
    index = 0
    duplicates = 0
    while index < size:
        if arr[index] == element :
            duplicates += 1
        else:
            for i in range(index, index + duplicates):
                arr[i-duplicates] = arr[i]
        index += 1
    print(duplicates)
    i = size-duplicates
    while i < size:
        arr[i] = 0
        i += 1
    return arr
a = removeDuplicate(source, 10, 2)
print(a)


#Task-7
#Splitting an Array
a = [1, 1, 1, 1, 2, 1, 1]
def sumCheck(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
        innersum = 0
        for j in range(i+1, len(arr)):
            innersum += arr[j]
        if sum == innersum:
            return True
    return False
sumCheck(a)


#Task-8 
# Array Series
n = [1, 2, 3, 4]
def arraySeries(n):
    newArr = [0] * (n*n)
    for i in range(1, n+1):
        for j in range(1, i+1):
            newArr[i*n-j] = j
    return newArr

a = arraySeries(len(n))
print(a)
        
		
		
#task-9
#maxBunchCount
def bunchCount(arr):
    count = 1
    newarr = [0]*len(arr)
    max = -9999999
    for i in range(len(arr)-1):    
        if arr[i] == arr[i+1]:
            count += 1
            newarr[i] = count
        else:
            count = 1
    for i in range(len(newarr)):
        if newarr[i] > max:
            max = newarr[i]
    return max
source = [int(item) for item in input()[1:-1].split(",")]
print(bunchCount(source))


#Task-10
#Repetition
def checkRepetition(arr):
    flag = False
    max = -9999999
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
    newArr = [0]*(max + 1)
    for i in range(len(arr)):
        if arr[i] < len(newArr):
            newArr[arr[i]] += 1
    for i in range(len(newArr)):
        for j in range(i+1, len(newArr)):
            if newArr[i] == newArr[j] and newArr[j] > 1:
                flag = True
    return flag

source = [int(item) for item in input()[1:-1].split(",")]
print(checkRepetition(source))