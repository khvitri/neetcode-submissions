class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = {0: 0, 1: 0, 2: 0}
        for num in nums:
            count[num] += 1
        
        def replaceNumVal(startIdx, valCount, val):
            for i in range(valCount):
                nums[startIdx + i] = val
        
        replaceNumVal(0, count[0], 0)
        replaceNumVal(count[0], count[1], 1)
        replaceNumVal(count[0] + count[1], count[2], 2)

        