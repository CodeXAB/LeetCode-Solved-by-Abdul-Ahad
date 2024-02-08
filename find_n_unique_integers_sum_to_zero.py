class Solution:
        def sumZero(self, n: int):
            result = []
            if n%2 != 0:
                result.append(0)
            for i in range(1,n//2 + 1):
                result.append(i)
                result.append(-i)
            return result


obj = Solution()

print(obj.sumZero(5))


'''
Time Complexity = O(n)
Space Complexity = O(n)
'''