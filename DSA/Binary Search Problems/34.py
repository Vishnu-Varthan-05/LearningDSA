def searchRange(nums, target):
    answer = [-1, -1]
    start = findSearch(nums, target, 1)
    end = findSearch(nums, target, 0)
    answer[0] = start
    answer[1] = end
    print("fuck u")
    return answer

def findSearch(nums, target, findStartIndex):
    answer = -1
    start_index = 0
    end_index = len(nums)-1

    while start_index <= end_index:
        middle_index = start_index + (end_index - start_index)//2

        if target > nums[middle_index]:
            start_index = middle_index + 1
        if target < nums[middle_index]:
            end_index = middle_index - 1
        if nums [middle_index] ==  target:
            answer = middle_index
            if findStartIndex :
                end_index = middle_index - 1
            else:
                start_index = middle_index + 1     

    return answer


nums = [5,7,7,8,8,10]
target = 8 
print(searchRange(nums, target))