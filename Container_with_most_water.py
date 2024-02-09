class Solution:
    def maxArea(self, height: list[int]):
        left,right,maxarea = 0, len(height) - 1, 0
        while left < right:
            area = min(height[left],height[right]) * (right - left)
            maxarea = max(maxarea,area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxarea

obj = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(obj.maxArea(height))


'''
1. We initialize two pointers, left and right, at the beginning and end of the array, respectively.
2. We iterate through the array using the two-pointer approach, calculating the area formed by the lines at left and right and updating max_area accordingly.
3. We move the pointer with the smaller height towards the center of the array, as moving the pointer with the larger height cannot lead to an increase in the area.
4. We continue this process until left is greater than or equal to right.
5. Finally, we return the max_area.

Time Complexity = O(n)
Space Complexity = O(1)
'''