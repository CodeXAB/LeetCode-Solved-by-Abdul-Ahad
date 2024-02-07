# Method 1
# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         return n>0  and (n&(n-1)) == 0
# using the bitwise AND operator

# Method 2
# class Solution:
#     def isPowerOfTwo(self, n: int):
#         if n<=0:
#             return False
#         return (n&(n-1)) == 0

# Method 3
# class Solution:
#     def isPowerOfTwo(self, n: int):
#         if n<=0:
#             return False
#         elif n == 1:
#             return True
#         elif n%2 == 0:
#             return self.isPowerOfTwo(int(n/2))
#         else:
#             return False


'''
Time Complexity = O(1)
Space Complexity = O(1)
'''