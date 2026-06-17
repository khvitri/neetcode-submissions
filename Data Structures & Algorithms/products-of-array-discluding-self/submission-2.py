class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Idea: The result at result[i] would be all the multiplication before that
        #  (prefix multiplication) multiply by all the multiplication after that
        #  (postfix multiplication).
        # 1. Loop over the nums list and calculate the necessary prefix multiplication
        #   to insert into result[i]
        # 2. Loop over the nums list in reverse order and calculate the necessary 
        #   postfix multiplication to insert into result[i]

        result = []
        prefixMult = 1
        for num in nums:
            result.append(prefixMult)
            prefixMult = prefixMult * num
        
        postfixMult = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] = result[i] * postfixMult
            postfixMult = postfixMult * nums[i]
        
        return result
            


            
            


        
        

        