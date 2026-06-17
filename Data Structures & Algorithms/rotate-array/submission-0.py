class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # rotate right: 2
        # replace left: 0
        # init idx: 1
        # swap idx: 1 (mod 8)
        # cur: 8
        # temp: 8
        # [7, 8, 1, 2, 3, 4, 5, 6]

        shiftR = k % len(nums)
        if shiftR == 0: return nums

        repLeft = len(nums)
        initIdx = 0
        while repLeft > 0:
            curNum = nums[initIdx]
            swapIdx = (initIdx + shiftR) % len(nums)
            while True:
                tempNum = nums[swapIdx]
                nums[swapIdx] = curNum
                curNum = tempNum
                swapIdx = (swapIdx + shiftR) % len(nums)
                repLeft -= 1 

                if swapIdx - shiftR == initIdx:
                    break

            initIdx += 1



        