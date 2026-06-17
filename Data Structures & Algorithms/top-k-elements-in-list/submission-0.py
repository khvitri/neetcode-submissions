class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Dictionary keeps count of each element
        # 2. Flip the keys and the values (i.e. the count becomes the key and the elements become the value)
        # 3. Elements with the same count are "grouped" into the same key
        result = []

        # Keeps track of number frequency
        nums_freq = defaultdict(int)    

        # Categorize the numbers based on frequency
        freq_bucket = defaultdict(list)

        for num in nums:
            nums_freq[num] += 1
        
        for num in nums_freq.keys():
            freq_bucket[nums_freq[num]].append(num)
        
        for i in range(len(nums), 0, -1):
            print(i)
            if i in freq_bucket:
                result = result + freq_bucket[i]
            
            if len(result) == k:
                return result

        
        return result


        


        
