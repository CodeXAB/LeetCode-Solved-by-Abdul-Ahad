class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums)-1
        while left<right:
            mid = (left+right)//2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid+1
        return nums[right]

''''
1. we don't need to sort the array
2. we apply binary search algorithm
3. we return the minimum value in the array

Time complexity O(log n)
Space minimum O(1)'''