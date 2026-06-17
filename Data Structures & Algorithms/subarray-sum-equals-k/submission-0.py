class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # [-1,3,-1,1,2]
        # prefix sum: [-1,2,1,2,4]
        # k = 2
        # sub arr count: 5
        # {
        #   -1: 1,
        #   1: 1,
        #   2: 2
        # }

        res = 0
        preNums = []
        prefix = 0
        for num in nums:
            prefix += num
            preNums.append(prefix)
        
        preNumsCount = dict()
        for num in preNums:
            if num == k:
                res += 1

            if num - k in preNumsCount:
                res += preNumsCount[num - k]
            
            preNumsCount[num] = 1 + preNumsCount.get(num, 0)
        
        return res


