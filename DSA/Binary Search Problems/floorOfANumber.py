def fbinarysearch(array, target):
    start_index = 0
    end_index = len(array) - 1

    if target < array[0]:
            return -1

    while start_index <= end_index:
        middle_index = start_index + (end_index - start_index)//2
    
        if target == array[middle_index]:
            return middle_index
        
        if target > array[middle_index]:
            start_index = middle_index + 1
        
        if target < array[middle_index]:
            end_index = middle_index - 1

    return array[end_index] 

array = [5, 6, 7, 8, 10, 24]
gtarget = int(input())
print(fbinarysearch(array, gtarget))