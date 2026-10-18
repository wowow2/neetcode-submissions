class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for string in strs:
            groups[tuple(sorted(string))].append(string)
        
        return list(groups.values())

            
        