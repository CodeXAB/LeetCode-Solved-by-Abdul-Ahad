class Solution:
    def isPalindrome(self, s: str):
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not self.alphanumeric(s[left]):
                left += 1
            while left < right and not self.alphanumeric(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left+=1
            right-=1
        return True

    def alphanumeric(self,character):
        return ("a"<=character<="z" or "A"<=character<="Z" or "0"<=character<="9")

obj = Solution()
print(obj.isPalindrome("A man, a plan, a canal: Panama"))