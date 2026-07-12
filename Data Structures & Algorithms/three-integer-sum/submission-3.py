class Solution:
    def _two_sum(self, nums: List[int], target: int) -> Optional[List[int]]:
        seen = set()
        pairs = []
        for num in nums:
            complement = target - num
            if complement in seen:
                pairs.append([complement, num])
            seen.add(num)
        return pairs

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        for i, num in enumerate(nums):
            pairs = self._two_sum(nums[i+1:], -num)
            for pair in pairs:
                triplet = tuple(sorted([num] + pair))
                res.add(triplet)
                
        return [list(i) for i in res]


        