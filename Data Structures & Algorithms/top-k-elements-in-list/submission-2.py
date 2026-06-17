class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        numToCount = {}
        countToNum = {}

        for num in nums:
            numToCount[num] = 1 + numToCount.get(num, 0)
        
        for num in numToCount.keys():
            countToNum[numToCount[num]] = [num] + countToNum.get(numToCount[num], []) 
        
        for count in range(len(nums), 0, -1):
            if count in countToNum:
                res += countToNum[count]
            
            if len(res) == k:
                return res
            
        return []
        