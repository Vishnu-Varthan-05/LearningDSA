def peakIndexInMountainArray(arr):
        start_index = 0
        end_index = len(arr)-1

        while start_index <= end_index:
            middle_index =  start_index + (end_index - start_index)//2 
            if (arr[middle_index] > arr[middle_index + 1]) and (arr[middle_index] > arr[middle_index - 1]):
                  return middle_index
            if arr[middle_index] > arr[middle_index + 1]:
                  end_index = middle_index 
            if arr[middle_index] < arr[middle_index + 1]:
                  start_index = middle_index + 1
        

arr = [0,5,4,3,2,1]
print(peakIndexInMountainArray(arr))