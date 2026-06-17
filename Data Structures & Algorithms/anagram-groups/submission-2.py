class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        anagGroup = {}

        for s in strs:
            sCount = {}
            for c in s:
                sCount[c] = 1 + sCount.get(c, 0)
            hashableSCount = frozenset(sCount.items())

            if hashableSCount in anagGroup:
                anagGroup[hashableSCount].append(s)
            else:
                anagGroup[hashableSCount] = [s]
                res.append(anagGroup[hashableSCount])
        
        return res
            


