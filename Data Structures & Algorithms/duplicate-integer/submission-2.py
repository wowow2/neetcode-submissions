class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return not len(list(set(nums))) == len(nums)  
        