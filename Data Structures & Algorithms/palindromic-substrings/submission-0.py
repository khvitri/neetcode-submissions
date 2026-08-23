class Solution:
    def countSubstrings(self, s: str) -> int:
        s = '#' + '#'.join(s) + '#' # Converts even length string to odd
        res = 0

        for i in range(len(s)):
            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if s[l] != '#':
                    res += 1
                l, r = l - 1, r + 1
        
        return res


