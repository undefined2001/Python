def merge(arr, left, middle, right):
    temp = [0] * len(arr)
    i: int = left
    j: int = middle + 1
    k: int = left
    while i <= middle and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            k += 1
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
            k += 1
    while i <= middle:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1
    for i in range(left, right + 1):
        arr[i] = temp[i]


def mergerSort(arr, left, right):
    if left >= right:
        return
    else:
        middle = (left + right) // 2
        mergerSort(arr, left, middle)
        mergerSort(arr, middle+1, right)
        merge(arr, left, middle, right)


if __name__ == "__main__":

    arr = [50, 40, 30, 20, 10, 60]

    mergerSort(arr, 0, len(arr)-1)


    print(arr)