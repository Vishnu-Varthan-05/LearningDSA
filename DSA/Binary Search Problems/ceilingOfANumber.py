def cbinarysearch(array, target):
    if target > array[len(array)-1]:
            return -1
    
    start_index = 0
    end_index = len(array) - 1

    while start_index <= end_index:
        middle_index = start_index + (end_index - start_index)//2
        
        if target == array[middle_index]:
            return middle_index
        
        if target > array[middle_index]:
            start_index = middle_index + 1
        
        if target < array[middle_index]:
            end_index = middle_index - 1

    return array[start_index] 

array = [1, 3, 13, 15, 19, 34]
gtarget = int(input())
print(cbinarysearch(array, gtarget))