class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # How do we know if the cars will meet each other before or on the target?
        # [1, 4]
        # 4 gets to 10 in 3 hours ((10 - 4) / 2)
        # 1 gets to 10 in 3 hours ((10 - 1) / 3)
        # => Distance Left / Speed
        # 
        # How do we know which car belongs to which fleet? 
        # [4, 1, 0, 7]
        # ETA: [3, 4.5, 10, 3]
        # Is there an O(n) solution that utilizes stack?
        # What does O(n log n) solution look like?
        # Sort it
        # [7, 4, 1, 0]
        # ETA: [3, 3, 4.5, 10]
        posSpeedPair = [(p, s) for p, s in zip(position, speed)]

        
        posSpeedPair.sort(reverse=True)

        stack = []
        for p, s in posSpeedPair:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)