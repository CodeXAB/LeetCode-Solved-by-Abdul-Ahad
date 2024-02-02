class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int):
        i,j,k = m-1, n-1, m+n-1
        while i>=0 and j>=0:
            if nums1[i]>nums2[j]:
                nums1[k] = nums1[i]
                i-=1
            else:
                nums1[k] = nums2[j]
                j-=1
            k-=1
        while j>=0:
            nums1[k] = nums2[j]
            j-=1
            k-=1

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
obj = Solution()
obj.merge(nums1, m, nums2, n)
print(nums1)

'''
How it works?
1. Initialize three pointers: i for nums1, j for nums2, and k for the merged array (starting from the end).
2. Compare elements from nums1 and nums2, and place the larger element at the end of nums1 (position k). Move the corresponding pointers accordingly.
3. Continue this process until one of the arrays is fully processed.
4. If there are remaining elements in nums2 after nums1 is processed, copy them to the beginning of nums1.
Time Complexity is O(m+n)
Space Complexity is O(1)

'''
