class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1

        res = -1
        for k in count.keys():
            if count[k] > 1:
                continue
            res = max(res, k)
        
        return res


