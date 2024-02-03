class Solution:
    def shortestToChar(self, s: str, c: str):
        occurence = []  # to track the number of occurences of the letter
        for i in range(len(s)):
            if s[i] == c:
                occurence.append(i)
        answer = []
        for i in range(len(s)):
            if s[i] == c:   # if it's character then the distance will be zero
                answer.append(0)
            else:
                temp = []   # this will track the distances of ith index to all the occurences of the letter
                for j in range(len(occurence)):
                    temp.append(abs(occurence[j] - i))
                min_dist = min(temp)    # getting the minimum distance
                answer.append(min_dist) # appending the minimum distance to the answer list
        return answer

obj = Solution()
print(obj.shortestToChar("loveleetcode","e"))


'''
How it works?
1. first we have to check the number of occurences of the given letter.
2. we need to calculate the distances.
3. if the ith index is the same given letter then the distance will be zero
4. if the ith index is some other letter then it will calculate distance from all the occurences of the given letter.
5. Finally appending the minimum distance of the letter to the list.

Time Complexity = O(n^2)
Space Complexity = O(n), because we are using additonal lists.
'''