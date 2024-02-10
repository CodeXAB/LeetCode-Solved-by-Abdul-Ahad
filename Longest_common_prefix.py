class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        # Initialize longest common prefix as the first string
        longest_prefix = strs[0]

        # Iterate through the characters of the reference string
        for i in range(len(longest_prefix)):
            # Compare the character at index i with corresponding characters in other strings
            for s in strs[1:]:
                # If any character doesn't match or string length is less than i+1, return the prefix up to index i
                if i >= len(s) or longest_prefix[i] != s[i]:
                    return longest_prefix[:i]

        # If all characters match, return the longest prefix itself
        return longest_prefix

obj = Solution()
strs = ["flower","flow","flight"]   # return fl
strs = ["dog","racecar","car"]  # return empty string
print(obj.longestCommonPrefix(strs))

'''
1. If the array of strings is empty, return an empty string.
2. Initialize the longest common prefix string as the first string in the array (the reference string).
3. Iterate through the characters of the reference string.
4. For each character at index i, compare it with the character at index i of the other strings in the array.
5. If all characters at index i match in all strings, append the character to the longest common prefix string.
6. If any character doesn't match or if the length of any string is less than i+1, return the longest common prefix string up to index i.
7. If all characters match in all strings up to the length of the shortest string, return the longest common prefix string itself.
'''