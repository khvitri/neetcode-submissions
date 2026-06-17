class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 4 pointers: a, b, c, d
        # "a" and "b" is a pair. "c" and "d" is a pair.
        # a < b < c < d

        # a: 1
        # b: 3 => c, d target: target - (num[a] + num[b]) = 4
        # c: 4
        # d: 5 => c, d sum: 6
        # target = 3
        # [-3,0,1,2,3,3]
        # [[-3, 0, 3, 3], [-3, 1, 2, 3]]
        if len(nums) < 4: return []

        nums.sort()
        res = []

        print(nums)

        # Stop 3 index before for b, c, and d.
        for a in range(len(nums) - 3):
            if a > 0 and nums[a] == nums[a - 1]: continue
            # Stop 2 index before end for c and d.
            for b in range(a + 1, len(nums) - 2):
                if b > a + 1 and nums[b] == nums[b - 1]: continue
                cdTarget = target - (nums[a] + nums[b])
                c, d = b + 1, len(nums) - 1
                while c < d:
                    if nums[c] + nums[d] == cdTarget:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        while nums[c] == nums[c - 1] and c < d:
                            c += 1
                    elif nums[c] + nums[d] > cdTarget:
                        d -= 1
                    else:
                        c += 1
        
        return res



        