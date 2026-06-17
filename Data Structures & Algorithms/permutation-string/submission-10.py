NUM_LOWERCASE = 26

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # For s2 to contain s1 as a permutation:
        #   1. The set of characters in s2 has to exist in s1
        #   2. The set of characters must be contiguous in s2
        #   3. The set of characters frequency must be the same amount as s1

        #   Why l != r when we realize a mismatch 
        #   s1 = "cab", s2 = "abac"
        if len(s2) < len(s1): return False
        
        matches = 0
        alphaLower = {chr(ord('a') + i) for i in range(NUM_LOWERCASE)}
        s1Count = {c: 0 for c in alphaLower}
        s2Count = {c: 0 for c in alphaLower}

        for i in range(len(s1)):
            s1Count[s1[i]] += 1
            s2Count[s2[i]] += 1
        
        for c in alphaLower:
            if s1Count[c] == s2Count[c]: matches += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == NUM_LOWERCASE: return True

            s2Count[s2[r]] += 1
            if s2Count[s2[r]] == s1Count[s2[r]]:
                matches += 1
            elif s2Count[s2[r]] == s1Count[s2[r]] + 1:
                matches -= 1

            s2Count[s2[l]] -= 1
            if s2Count[s2[l]] == s1Count[s2[l]]:
                matches += 1
            elif s2Count[s2[l]] == s1Count[s2[l]] - 1:
                matches -= 1
            l += 1

        return matches == NUM_LOWERCASE
            
            
        
