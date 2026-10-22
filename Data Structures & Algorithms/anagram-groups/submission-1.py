class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = 0
        groups = {}

        for i in range(len(strs)):
            elem = strs[i]
            key = "".join(sorted(elem)) #returns a sorted string
            if key in groups:
                groups[key].append(elem)
            else:
                groups[key] = [elem]
        return list(groups.values())