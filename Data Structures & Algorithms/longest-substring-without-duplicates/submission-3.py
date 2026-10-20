class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = left = 0
        seen = {}
        for index, char in enumerate(s):
            if char in seen:
                left = max(left, seen[char] + 1)
            seen[char] = index
            longest_substring = max(longest_substring, index - left + 1)
        return longest_substring