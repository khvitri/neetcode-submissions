class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Match the heaviest with the lightest
        # If heaviest + lightest > limit, then best solution is heavist
        #   alone in boat

        people.sort()

        # leftmost = lightest, rightmost = heaviest
        l, r = 0, len(people) - 1
        noBoat = 0

        while l <= r:
            pairWeight = people[l] + people[r]

            # Heaviest can pair with lightest
            if pairWeight <= limit:
                l += 1                
            r -= 1
            noBoat += 1
        
        return noBoat
