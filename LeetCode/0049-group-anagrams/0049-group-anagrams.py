class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups ={}

        for x in strs:
            key = tuple(sorted(x))
            if key not in groups:
                groups[key] = []
            groups[key].append(x)
        return list(groups.values())
            

        