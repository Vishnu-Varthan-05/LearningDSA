def find_min(nums):
    start=0
    end = len(nums)-1
    if nums[start]<nums[end]: 
        return nums[start]
    while(start+1 < end):
        mid = start + (end - start) // 2
        if(nums[mid]>nums[end]):
            start = mid
        else: 
            end = mid

    return min(nums[start],nums[end])


nums = [4,5,6,1,2,3]
# nums = [11,13,15,17]
print(find_min(nums))




