class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = 0
        left = 0
        last_seen = {}
        for index, char in enumerate(s):
            if char in last_seen:
                left = max(left, last_seen[char] + 1)
            last_seen[char] = index
            longest_substring = max(longest_substring, index - left + 1)
        return longest_substring