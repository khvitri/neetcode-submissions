class Solution:
    def isValid(self, s: str) -> bool:
        bracketPairs = {'(': ')', '{': '}', '[': ']'}

        stack = []
        for c in s:
            if c in bracketPairs:
                stack.append(c)
                continue 

            if len(stack) <= 0 or bracketPairs[stack.pop()] != c:
                return False
        
        return len(stack) == 0
        