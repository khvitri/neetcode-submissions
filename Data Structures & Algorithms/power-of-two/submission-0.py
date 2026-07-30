class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        l, r = 0, 31
        while l <= r:
            m = (l + r) // 2

            if 2**m > n:
                r = m - 1
            elif 2**m < n:
                l = m + 1
            else:
                return True

        return False