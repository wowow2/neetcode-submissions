class Solution:
    def _hours_needed(self, piles: List[int], k):
        return sum(-(-pile //k) for pile in piles)

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if self._hours_needed(piles, mid) <= h:
                right = mid 
            else:
                left = mid + 1 
        return right