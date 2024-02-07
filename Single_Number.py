class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0 # n ^ 0 = n
        for n in nums:
            result ^= n
        return result
obj = Solution()
nums = [4,2,1,2,1]
print(obj.singleNumber(nums))

'''
1. We have to solve it in linear time
2. we are using bit wise XOR operator (n ^ 0 = n)
3. comparing binary value of every element with the result and return the final value

Time complexity = O(n)
Space Complexity = O(1)

'''