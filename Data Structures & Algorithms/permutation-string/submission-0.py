class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        need = Counter(s1)
        window = Counter(s2[:len(s1)])

        if need == window:
            return True
        
        for i in range(len(s1), len(s2)):
            add_char = s2[i]
            remove_char = s2[i - len(s1)]

            window[add_char] += 1
            window[remove_char] -= 1

            if need == window:
                return True
        return False

