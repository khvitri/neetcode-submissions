class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # For s2 to contain s1 as a permutation:
        #   1. The set of characters in s2 has to exist in s1
        #   2. The set of characters must be contiguous in s2
        #   3. The set of characters frequency must be the same amount as s1

        #   Why l != r when we realize a mismatch 
        #   s1 = "cab", s2 = "abac"

        s1Freq = defaultdict(int)
        for c in s1:
            s1Freq[c] += 1

        l, r = 0, 0
        s2PermFreq = defaultdict(int)
        while r < len(s2):
            if s2[r] in s1Freq:
                if len(s2PermFreq) != 0:
                    while s2PermFreq[s2[r]] + 1 > s1Freq[s2[r]] and l <= r:
                        s2PermFreq[s2[l]] -= 1
                        l += 1                    
                else:
                    l = r
                s2PermFreq[s2[r]] += 1
            else:
                s2PermFreq = defaultdict(int)
            
            if s2PermFreq == s1Freq:
                return True

            print(s2PermFreq)
            r += 1
        
        return False

