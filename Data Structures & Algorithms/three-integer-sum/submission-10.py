class Solution:
    def _twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        seen = set()
        output = set()
        for num in nums:
            complement = target - num
            if complement in seen:
                output.add((min(num, complement), max(num, complement)))
            seen.add(num)
        return [list(p) for p in output]

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        for i in range(len(nums)):
            for pair in self._twoSum(nums[i + 1:], -nums[i]):
                result.add(tuple(sorted(pair + [nums[i]])))
        return [list(t) for t in result]
            
        