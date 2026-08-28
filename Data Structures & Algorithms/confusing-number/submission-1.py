class Solution:
    def confusingNumber(self, n: int) -> bool:
        invalid = {"2", "3", "4", "5", "7"}

        s = str(n)[::-1]
        res = [""] * len(s)

        for i in range(len(s)):
            if s[i] in invalid:
                return False
            
            if s[i] == "9":
                res[i] = "6"
            elif s[i] == "6":
                res[i] = "9"
            else:
                res[i] = s[i]
        
        return int("".join(res)) != n



