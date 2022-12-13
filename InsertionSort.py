def checker(prev_index, arr, current_index):
    # if previous less than current index then it will be considered sorted and 
    # it will exit the recursion
    if prev_index < 0 or arr[current_index] > arr[prev_index]:
        return
    
    #keep swaping value if current index is lower than the previous one
    temp = arr[current_index]
    arr[current_index] = arr[prev_index]
    arr[prev_index] = temp
  
    checker(prev_index-1, arr, current_index-1)

def insertionRecursion(arr, idx = 1):
    if idx == len(arr):
        return arr
    else:    
        j = idx -1
        checker(j, arr, idx)
        return insertionRecursion(arr, idx +1)
    
    
    
array = [-1,-2, 3, -5, 4, 9, 8, 7, -10]
print(insertionRecursion(array))