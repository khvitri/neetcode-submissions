class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}
        for i in range(len(words)):
            if i + 1 < len(words):
                a, b = words[i], words[i + 1]
                for j in range(len(a)):
                    if j >= len(b):
                        return ""

                    if a[j] != b[j]:
                        adj[b[j]].add(a[j]) 
                        break
        
        visit, path = set(), set()
        res = []

        def dfs(node: str) -> bool:
            if node in path:
                return False
            if node in visit:
                return True
            
            visit.add(node)
            path.add(node)
            for neigh in adj[node]:
                if not dfs(neigh):
                    return False
            path.remove(node)
            res.append(node)
            return True
        
        for node in adj.keys():
            if not dfs(node):
                return ""
        
        return ''.join(res)

        

