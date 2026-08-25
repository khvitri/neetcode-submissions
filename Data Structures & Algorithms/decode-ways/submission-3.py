class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0": return 0

        # Track counts of valid "groups" ending at current index
        # q[val] = count of ways to have 'val' as the last group
        q = {s[0]: 1}

        for i in range(1, len(s)):
            new_q = Counter()
            if not q:
                return 0
            
            for group, count in q.items():
                # Decide to not group (start fresh with s[i])
                if s[i] != "0":
                    new_q[s[i]] += count
                 
                # Decide to group (combine existing group with s[i])
                if len(group) != 2 and int(group + s[i]) <= 26:
                    new_q[group + s[i]] += count
            q = new_q
        
        return sum(q.values())