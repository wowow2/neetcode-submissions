class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        best = 0
        for right, char in enumerate(s):
            count[char] = count.get(char,0) + 1
            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            best = max(best, right - left + 1)
        return best