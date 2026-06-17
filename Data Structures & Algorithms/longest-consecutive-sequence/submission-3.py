class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set()
        for num in nums:
            numsSet.add(num)

        res = 0
        for num in nums:
            # We know that this is the start of a sequence
            if num - 1 not in numsSet:
                curSeqLen = 1
                curNum = num + 1
                while curNum in numsSet:
                    curNum += 1
                    curSeqLen += 1
                res = max(res, curSeqLen)
        
        return res

                


        