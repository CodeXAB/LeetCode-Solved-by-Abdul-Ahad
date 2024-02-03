class Solution:
    def findDisappearedNumbers(self, nums: list[int]):
        num_set = set(nums)
        answer = []
        for i in range(1,len(nums)+1):
            if i not in num_set:
                answer.append(i)
        return answer

obj = Solution()
print(obj.findDisappearedNumbers([4,3,2,7,8,2,3,1]))

'''
1. first we convert list into set so that repeated number can be neglected.
2. we need to loop equal to the number of elements (not iterating on the list)
3. checking if the ith element is not in set.
4. if not, then we will append it to the list.

Time Complexity= O(n)
Space Complexity= O(n)
'''