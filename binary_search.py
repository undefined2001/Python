def binary_search(arr, left, right, val):
    if left > right:
        return -1
    
    mid = (left+right)//2
    if arr[mid] == val:
        return f"{val} exists"
    elif arr[mid] > val:
        return binary_search(arr, left, mid - 1, val)
    else:
        return binary_search(arr, mid + 1, right, val)


arr = [2,5, 15, 20, 30, 40, 50]

print(binary_search(arr, 0, len(arr)-1, int(input("enter A Number: "))))
