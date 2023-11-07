#return index if exist
#return -1 if doesnt exist 
def binarysearch(array, target):
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

    return -1 

array = [1, 3, 13, 15, 19, 34]
print(binarysearch(array, 34))