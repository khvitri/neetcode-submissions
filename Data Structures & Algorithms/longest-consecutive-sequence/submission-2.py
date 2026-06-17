class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        numsSet = set()
        for num in nums:
            numsSet.add(num)

        maxSeq = 1
        for num in numsSet:
            if (num - 1) in numsSet:
                continue
            
            curSeq, curNum = 1, num + 1
            while curNum in numsSet:
                curSeq += 1
                curNum += 1
            
            if curSeq > maxSeq:
                maxSeq = curSeq

        return maxSeq


            



                


        