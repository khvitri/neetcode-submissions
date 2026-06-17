class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set()
        for num in nums:
            numsSet.add(num)
        
        temp = list(numsSet)
        maxSeq = 0
        for num in temp:
            if num not in numsSet:
                continue
            curSeq = 1
            numsSet.remove(num)
            left, right, leftNum, rightNum = True, True, num - 1, num + 1
            while left or right:
                left = leftNum in numsSet
                right = rightNum in numsSet

                if left:
                    numsSet.remove(leftNum)
                    curSeq += 1
                    leftNum -= 1
                    
                
                if right:
                    numsSet.remove(rightNum)
                    curSeq += 1
                    rightNum += 1
            
            if curSeq > maxSeq:
                maxSeq = curSeq
        
        return maxSeq



                


        