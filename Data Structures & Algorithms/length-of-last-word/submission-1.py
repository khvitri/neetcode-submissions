class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                continue
            
            j = i
            while j >= 0 and s[j] != " ":
                j -= 1
                count += 1
            
            return count
        
        return count

            