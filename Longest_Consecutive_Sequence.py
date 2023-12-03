# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

class Solution:
    def longestConsecutive(self, nums) -> int:
        numSet = set(nums)  # converting into set to avoid repetition of numbers.
        longest = 0
        for n in numSet:   # iterating to each element.
            if (n-1) not in numSet: # if a number less the current element is not present
                length = 1  # it means the current element is the first element o fthe sequence.
                while (n+length) in numSet: # now checking if the numbers after the current element are present to make the sequence.
                    length+=1   # if they are present then length will be increased with each element
                longest = max(length,longest)   # now declaring the longest sequence.
        return longest

nums = [100,4,200,1,3,2]
ans = Solution()
print(ans.longestConsecutive(nums))
# The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.