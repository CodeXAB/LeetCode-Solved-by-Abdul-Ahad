class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        for i in range(1,len(nums)):
            nums[i] = nums[i-1] + nums[i]
        return nums
obj = Solution()
nums = [1,2,3,4]
print(obj.runningSum(nums))


'''
1. we are letting the first element on 0th index as it is.
2. we are now standing at the 1st index.
3. then the element of 1st index will be added to the element of 0th index.
4. this process will be repeated for all elements

Time complexity = O(n)
Space Complexity = O(1)
'''