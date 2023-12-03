# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


# class Solution:
#     def twoSum(self, nums, target: int):
#         num_dict = {}  # Dictionary to store seen numbers and their indices
#         for i, num in enumerate(nums):
#             complement = target - num
#             # If the complement is in the dictionary, return its index along with the current index
#             if complement in num_dict:
#                 return [num_dict[complement], i]
#             # If complement is not in the dictionary, add the current number and its index to the dictionary
#             num_dict[num] = i
#         # If no solution is found
#         return []
    

# Second implementation:
# class Solution:
#     def twoSum(self, nums, target: int):
#         result = []
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[j] == target - nums[i]:
#                     result.append(i)
#                     result.append(j)
#         return result
