class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphaChar = set()
        for i in range(26):
            alphaChar.add(chr(ord('A') + i))
            alphaChar.add(chr(ord('a') + i))

        for i in range(10):
            alphaChar.add(chr(ord('0') + i))

        # Remove all the non-alphanumeric characters
        alphaStr = ''
        for c in s:
            if c in alphaChar:
                alphaStr += c.lower()
        
        left = 0
        right = len(alphaStr) - 1
        while left < right and left != right:
            if alphaStr[left] != alphaStr[right]:
                return False
            left += 1
            right -= 1
        
        return True

        