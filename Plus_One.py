class Solution:
    def plusOne(self, digits: list[int]):
        n = len(digits)
        for i in range(n-1,-1,-1):  # iterating to list in reverse order
            if digits[i]<9: # if the last digit is less than 9
                digits[i]+=1   # then we will increment the number by 1
                return digits
            digits[i] = 0   # if the last number and if it's leading number is 9 then declare it to 0
        return [1] + digits
obj = Solution()
print(obj.plusOne([1,0,9,4]))

# time complexity is O(n) where n is the length of the list
# Space complexity is O(1) because we use the same list