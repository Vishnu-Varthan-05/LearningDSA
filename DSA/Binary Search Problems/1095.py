class MountainArray:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index: int) -> int:
        return self.arr[index]

    def length(self) -> int:
        return len(self.arr)

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        def binary_search(mountainArr, target, start, end, ascending):
            while start <= end:
                middle_index = (start + end) // 2
                middle_val = mountainArr.get(middle_index)

                if middle_val == target:
                    return middle_index

                if ascending:
                    if middle_val < target:
                        start = middle_index + 1
                    else:
                        end = middle_index - 1
                else:
                    if middle_val > target:
                        start = middle_index + 1
                    else:
                        end = middle_index - 1

            return -1

        start_index, end_index = 0, mountainArr.length() - 1
        while start_index < end_index:
            middle_index = (start_index + end_index) // 2
            if mountainArr.get(middle_index) < mountainArr.get(middle_index + 1):
                start_index = middle_index + 1
            else:
                end_index = middle_index

        peak_index = start_index

        ascending_result = binary_search(mountainArr, target, 0, peak_index, True)
        if ascending_result == -1:
            descending_result = binary_search(mountainArr, target, peak_index, mountainArr.length() - 1, False)
            return descending_result

        return ascending_result

array = [1, 2, 3, 4, 5, 3, 1]
target = 3
mountainArr = MountainArray(array)
solution = Solution()
result = solution.findInMountainArray(target, mountainArr)
print(result)
