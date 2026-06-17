class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # numbers list is in ascending order
        # numbers[idx1] + numbers[idx2] = target
        # numbers[idx1] and numbers[idx2] can be negative and positive
        # solution must be in O(1) space
        # the first index will always be the smallest number
        # the first two index will produce the smallest sum
        # the last two index will produce the biggest sum
        # does the first index and the third index produce the second smallest number?
        # [1, 2, 3, 4]
        # 3
        # 4
        # 5
        # 6
        # 7
        # [-3, -2, -1, 10]
        # -5
        # -4
        # 7
        # -3
        # 8
        if len(numbers) < 2:
            return [-1, -1]

        if len(numbers) == 2:
            return [1, 2]
        
        left = 0
        right = 1

        while right < len(numbers):
            total = numbers[left] + numbers[right] 
            if total == target:
                return [left + 1, right + 1]
            elif total > target:
                break
            
            if right == len(numbers) - 1:
                break
            else:
                right += 1
        
        while left < right:
            total = numbers[left] + numbers[right]
            if total > target:
                right -= 1
            elif total < target:
                left += 1
            else:
                return [left + 1, right + 1]

        return [-1, -1]
        