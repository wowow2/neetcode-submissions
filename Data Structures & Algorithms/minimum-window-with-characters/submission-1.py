class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        need = Counter(t)
        have = Counter()

        left = 0
        best_length = float('inf')
        satisfied = 0
        need_count = len(need)
        best_start = 0

        for right, char in enumerate(s):
            have[char] += 1

            if (char in need) and (have[char] == need[char]):
                satisfied += 1
            
            while satisfied == need_count:
                if (right - left + 1) < best_length:
                    best_length = right - left + 1
                    best_start = left
                if s[left] in need and have[s[left]] == need[s[left]]:
                    satisfied -= 1

                have[s[left]] -= 1
                left+=1
        if best_length == float('inf'):
            return ""
        return s[best_start : best_start + best_length]



        