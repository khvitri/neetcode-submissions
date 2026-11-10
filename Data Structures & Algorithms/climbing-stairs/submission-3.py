class Solution:
    def climbStairs(self, n: int) -> int:
        # Number of ways to climb n steps is:
        #   No. of ways to climb n - 1 step +
        #       No. of ways to climb n - 2 step

        # Start with 1 step: 1 way to climb 1 step
        # 2 step: 2 way to climb 2 step
        # 3 step: 1 step + 2 step = 3 way to climb
        # ...
        # n step: n - 1 step + n - 2 step

        one, two = 1, 1 # step 0, step 1

        # Starts at step 2
        for i in range(2, n+1):
            temp = one
            one = two
            two = two + temp
        
        return two