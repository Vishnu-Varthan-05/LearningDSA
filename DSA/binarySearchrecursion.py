def binaryRecursion(arr, start, end, target):
    if start > end:
        return -1
    middle = start + (end - start)//2
    if target == arr[middle]:
        return middle
    if target > arr[middle]:
        return binaryRecursion(arr, middle + 1, end, target)
    else:
        return binaryRecursion(arr, start, middle-1, target)
    
arr = [2, 5, 9, 10]
print(binaryRecursion(arr, 0, len(arr)-1, 10))