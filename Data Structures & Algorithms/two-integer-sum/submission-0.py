class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker: Dict[int, int] = dict()

        for i in range(len(nums)):
            num = nums[i]
            partner = target - num
            if partner in tracker:
                return [tracker[partner], i]
            tracker[num] = i
        
        raise ValueError("There must be exactly one pair")
            
        