class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1

        res = -1
        for k, v in count.items():
            if v > 1: continue
            res = max(res, k)
        
        return res


