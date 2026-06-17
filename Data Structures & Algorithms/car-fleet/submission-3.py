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
        fleetCount = 0

        posEtaArr = []
        for i in range(len(position)):
            iEta = (target - position[i]) / speed[i]
            posEtaArr.append((position[i], iEta))
        
        posEtaArr.sort(reverse=True)

        maxEta = 0
        for i in range(len(posEtaArr)):
            if i > 0 and maxEta >= posEtaArr[i][1]:
                continue
            fleetCount += 1
            maxEta = max(posEtaArr[i][1], maxEta)
        
        return fleetCount