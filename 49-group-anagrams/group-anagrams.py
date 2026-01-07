class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        
        for ch in strs:
            sortword = "".join(sorted(ch))
            if sortword in dict1:
                dict1[sortword] += [ch]
            else:
                dict1[sortword] = [ch]
        return list(dict1.values())

        