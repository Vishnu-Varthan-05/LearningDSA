def findTarget(nums, target):
    if len(nums) == 0:
        return -1

    start_index = 0
    end_index = len(nums) - 1

    while start_index < end_index:
        middle_index = start_index + (end_index - start_index) // 2
        if nums[middle_index] > nums[end_index]:
            start_index = middle_index + 1
        else:
            end_index = middle_index
    
    pivot_index = start_index
    # print(nums[pivot_index])
    start_index = 0
    end_index = len(nums) - 1

    if target >= nums[pivot_index] and target <= nums[end_index]:
        start_index = pivot_index
    else:
        end_index = pivot_index - 1

    while start_index <= end_index:
        middle_index = start_index + (end_index - start_index) // 2
        if nums[middle_index] == target:
            return middle_index
        elif nums[middle_index] < target:
            start_index = middle_index + 1
        else:
            end_index = middle_index - 1

    return -1  

 
nums = [4,5,6,7,1,2]
target = 5
print(findTarget(nums, target))
