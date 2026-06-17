class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forwardMult = []
        backwardMult = []
        
        for i in range(0, len(nums) - 1):
            iReverse = len(nums) - i - 1
            if i == 0:
                forwardMult.append(nums[i])
                backwardMult.append(nums[iReverse])
                continue
            
            forwardMult.append(forwardMult[i - 1] * nums[i])
            backwardMult.append(backwardMult[i - 1] * nums[iReverse])
        
        result = []
        for i in range(0, len(nums)):
            # i represents no. of elements to the left of i
            # iReverse represents no. of elements to the right of i
            iReverse = len(nums) - 1 - i
            if i - 1 < 0:
                result.append(backwardMult[iReverse - 1])
            elif iReverse - 1 < 0:
                result.append(forwardMult[i - 1])
            else:
                result.append(forwardMult[i - 1] * backwardMult[iReverse - 1])
        return result

        
        

        