# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]

# class Solution:
#     def getConcatenation(self, nums):
#         ans = []
#         # first loop to iterate 2 times in the array
#         for i in range(2):
#             # second loop to iterate through each element in the loop
#             for j in nums:
#                 ans.append(j)
#         return ans
    
# a  = [1,2,3]
# obj = Solution()
# print(obj.getConcatenation(a))

# Second Implementation
# class Solution:
#     def getConcatenation(self, nums):
#             ans = nums
#             for i in range(len(nums)):
#                   ans.append(nums[i])
#             return ans
# obj = Solution()
# print(obj.getConcatenation([1,2,1,5]))