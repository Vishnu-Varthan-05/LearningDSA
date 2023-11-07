#Given an array nums of integers, return how many of them contain an even number of digits.
# nums = [555,901,482,1771]
# answer = 0

# def value_length(local_value):
#     length = 0 
#     while (local_value>0):
#         length += 1
#         local_value = local_value//10
#     return length
# for values in nums:
#     if value_length(values) % 2 == 0:
#         answer += 1 

# print(answer)

# or 
import math

nums = [555,901,482,1771]
answer = 0

for values in nums:
    count = math.floor(math.log10(values)) + 1  
    if count % 2 == 0:
        answer += 1 



