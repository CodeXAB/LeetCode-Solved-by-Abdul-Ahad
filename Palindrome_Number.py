# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.



class Solution:
    def isPalindrome(self, x: int):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_num, original_num = 0, x
        
        while x > 0:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
        
        return reversed_num == original_num
    
obj = Solution()
print(obj.isPalindrome(121))