class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Idea: The result at result[i] would be all the multiplication before that
        #  (prefix multiplication) multiply by all the multiplication after that
        #  (postfix multiplication).
        # 1. Loop over the nums list and calculate the necessary prefix multiplication
        #   to insert into result[i]
        # 2. Loop over the nums list in reverse order and calculate the necessary 
        #   postfix multiplication to insert into result[i]

        result = [1] * len(nums)
        prefixMult = 1
        for i in range(0, len(nums)):
            result[i] = result[i] * prefixMult
            prefixMult = prefixMult * nums[i]
        
        postfixMult = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] = result[i] * postfixMult
            postfixMult = postfixMult * nums[i]
        
        return result
            


            
            


        
        

        