class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)

    # Divide and conquer, merge sort. Return sorted array
    def mergeSort(self, nums: List[int]) -> List[int]:
        lSorted, rSorted = None, None

        if len(nums) > 1:
            lSorted = self.mergeSort(nums[:len(nums) // 2])
            rSorted = self.mergeSort(nums[len(nums) // 2:])
        else:
            return [nums[0]]
        
        sortedArr = []
        lIdx, rIdx = 0, 0
        while lIdx < len(lSorted) and rIdx < len(rSorted):
            if lSorted[lIdx] <= rSorted[rIdx]:
                sortedArr.append(lSorted[lIdx])
                lIdx += 1
            else:
                sortedArr.append(rSorted[rIdx])
                rIdx += 1
        
        if lIdx < len(lSorted):
            sortedArr = sortedArr + lSorted[lIdx:]
        elif rIdx < len(rSorted):
            sortedArr = sortedArr + rSorted[rIdx:]
        
        return sortedArr



        