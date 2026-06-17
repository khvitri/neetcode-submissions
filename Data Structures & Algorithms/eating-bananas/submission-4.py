class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # piles = [1, 4, 3, 2], h = 9, k = 2
        # h1: [0, 4, 3, 2]
        # h2: [0, 2, 3, 2]
        # h3: [0, 0, 3, 2]
        # h4: [0, 0, 1, 2]
        # h5: [0, 0, 0, 2]
        # h6: [0, 0, 0, 0]

        # piles = [1, 4, 3, 2], h = 9, k = 1
        # h1: [0, 4, 3, 2]
        # h2: [0, 3, 3, 2]
        # h3: [0, 2, 3, 2]
        # h4: [0, 1, 3, 2]
        # h5: [0, 0, 3, 2]
        # h6: [0, 0, 2, 2]
        # h7: [0, 0, 1, 2]
        # h8: [0, 0, 0, 2]
        # h9: [0, 0, 0, 1]

        # piles = [25, 10, 23, 4], h = 4
        # midpoint = k = 12
        # h1 = [13, 10, 23, 4]
        # h2 = [1, 10, 23, 4]
        # h3 = [0, 10, 23, 4]
        # h4 = [0, 0, 23, 4]

        # piles = [25, 10, 23, 4], h = 4
        # midpoint = k = 19
        # h1 = [6, 10, 23, 4]
        # h2 = [0, 10, 23, 4]
        # h3 = [0, 0, 23, 4]
        # h4 = [0, 0, 4, 4]

        # n: the num. of piles
        # m: max number of pile of bananas within the piles
        # n log m 

        left, right = 1, max(piles)
        k = 0

        while left <= right and piles:
            mid = (right + left) // 2

            hSpent = 0
            for bananas in piles:
                hSpent += math.ceil(bananas / mid) 
            
                if hSpent > h:
                    break 
            
            if hSpent > h:
                left = mid + 1
            elif hSpent <= h:
                k = mid
                right = mid - 1
        
        return k

            
