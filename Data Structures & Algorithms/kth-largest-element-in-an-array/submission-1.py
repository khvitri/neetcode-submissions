class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            raise Exception('nums list is empty')
        
        kMinHeap = [nums[0]]
        heapq.heapify(kMinHeap)

        for i in range(1, len(nums)):
            if len(kMinHeap) < k:
                heapq.heappush(kMinHeap, nums[i])
            elif nums[i] > kMinHeap[0]:
                heapq.heappush(kMinHeap, nums[i])
            
            if len(kMinHeap) > k:
                heapq.heappop(kMinHeap)
        
        return kMinHeap[0]