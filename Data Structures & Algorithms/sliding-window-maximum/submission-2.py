class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque()

        for r in range(k):
            while q and q[-1] < nums[r]:
                q.pop()
            q.append(nums[r])
        
        
        res.append(q[0])

        l = 0
        for r in range(k, len(nums)):
            if q and q[0] == nums[l]:
                q.popleft()
            l += 1

            while q and q[-1] < nums[r]:
                q.pop()
            q.append(nums[r])
            res.append(q[0])
        
        return res


