class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = {}
        for num in nums:
            numCount[num] = 1 + numCount.get(num, 0)
        
        numsSortedByCount = sorted(numCount.items(), key=lambda item: item[1], reverse=True)

        return [num[0] for num in numsSortedByCount[:k]]
        