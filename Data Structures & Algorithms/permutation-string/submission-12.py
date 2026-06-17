class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Permutation: To contain the exact amount of characters as the other word.
        #   Ignores ordering.
        # Count char. freq. in s1 using hashmap (H1)
        # Count char. freq. for window in s2 using hashmap (H2)
        # If H1 == H2, then return true
        # If that never happens throughout s2, return false
        # O(26 * n)
        # A variable that stores total characters matched so far. Update this variable
        #   everytime we update the window in s2. If variable is equal to 26, then all
        #   character count matched and return True
        if len(s2) < len(s1): return False

        LOWERCASE_SIZE  = 26
        matched = LOWERCASE_SIZE
        s1Count = {chr(ord('a') + c): 0 for c in range(LOWERCASE_SIZE)}
        s2WinCount = {chr(ord('a') + c): 0 for c in range(LOWERCASE_SIZE)}

        for i in range(len(s1)):
            s1Count[s1[i]] += 1
            s2WinCount[s2[i]] += 1 
        
        # Update the matched variable
        for c in s1Count.keys():
            if s1Count[c] != s2WinCount[c]:
                matched -= 1
            
        # Window size is len(s1)
        l = 0
        for r in range(len(s1), len(s2)):
            if matched == LOWERCASE_SIZE: return True

            s2WinCount[s2[r]] += 1
            if s2WinCount[s2[r]] - 1 == s1Count[s2[r]]:
                matched -= 1
            elif s2WinCount[s2[r]] == s1Count[s2[r]]:
                matched += 1
            
            s2WinCount[s2[l]] -= 1
            if s2WinCount[s2[l]] + 1 == s1Count[s2[l]]:
                matched -= 1
            elif s2WinCount[s2[l]] == s1Count[s2[l]]:
                matched += 1
            l += 1
            
        return matched == LOWERCASE_SIZE
        
        