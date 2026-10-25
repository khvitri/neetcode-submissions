class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            count = tuple(count)
            anagramDict[count].append(s)
        
        res = []
        for k in anagramDict.keys():
            res.append(anagramDict[k])
        
        return res
