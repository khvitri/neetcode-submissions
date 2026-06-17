class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Keep a count of elements in nums
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        # Flipping the key-value pair of count 
        freq = defaultdict(list)
        for key in count.keys():
            freq[count[key]].append(key)
        
        res = []
        for i in range(len(nums)):
            if len(nums) - i in freq:
                res = res + freq[len(nums) - i]
            
            if len(res) >= k:
                return res
        
        return res
        
        



        


        
