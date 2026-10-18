class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        most_common = Counter(nums).most_common(k)
        return [x[0] for x in most_common]

        