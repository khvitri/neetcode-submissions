class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mulTotal = 1 if len(nums) > 0 else 0
        zero_count = 0
        for num in nums:
            if num != 0:
                mulTotal = mulTotal * num
            else:
                zero_count += 1

            if zero_count > 1:
                return [0] * len(nums)

        result = []
        for num in nums:
            if zero_count and num != 0:
                result.append(0)
            elif zero_count and num == 0:
                result.append(mulTotal)
            else:
                result.append(mulTotal // num)
        
        return result
        