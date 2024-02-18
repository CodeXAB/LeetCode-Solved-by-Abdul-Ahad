class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        max_so_far = max_ending_here = nums[0]

        for num in nums[1:]:
            max_ending_here += num
            if num > max_ending_here:
                max_ending_here = num
            if max_ending_here > max_so_far:
                max_so_far = max_ending_here

        return max_so_far

# Example usage:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum subarray sum:", max_subarray_sum(nums))



'''
We initialize two variables, max_so_far and max_ending_here, to the first element of the input array nums. These variables represent the maximum subarray sum found so far and the maximum sum ending at the current position, respectively.
Iteration:

We iterate through the input array nums starting from the second element.
For each element num in the array:
We add num to max_ending_here, which represents the sum of the subarray ending at the current position.
We compare num with max_ending_here. If num is greater than max_ending_here, it means starting a new subarray from num would be better than extending the current subarray. Therefore, we update max_ending_here to num.
We then compare max_ending_here with max_so_far. If max_ending_here is greater than max_so_far, it means we've found a new maximum subarray sum. Therefore, we update max_so_far to max_ending_here.
Return:

Once we've iterated through the entire array, we return max_so_far, which represents the maximum subarray sum found.


Time complexity O(n)
Space complexity O(1)
'''
