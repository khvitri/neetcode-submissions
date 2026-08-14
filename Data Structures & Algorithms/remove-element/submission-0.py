class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        r = 0
        for l in range(len(nums)):
            if nums[l] == val:
                if r < l: r = l
                while r < len(nums) and nums[r] == val:
                    r += 1
                
                if r >= len(nums):
                    break
                    
                nums[l] = nums[r]
                nums[r] = val
        
        cnt = 0
        for i in range(len(nums)):
            if nums[i] == val:
                break
            cnt += 1 
        
        return cnt
        

                  