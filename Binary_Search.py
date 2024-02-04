class Solution:
    def BinarySearch(self,nums: list[int], target: int):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
        return -1
obj = Solution()
print(obj.BinarySearch([-1,0,3,5,9,12],9))

'''
Time Complexity = O(log n)
Space Complexity = O(1)

'''