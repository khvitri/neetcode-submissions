class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
    
        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
    
        visited = set()
        
        def dfs(root):
            stack = [root]
            
            while stack:
                node = stack.pop()
                
                if node in visited:
                    continue
                
                visited.add(node)
                
                for other in adj[node]:
                    stack.append(other)
        
        for node in range(n):
            if node in visited:
                continue
               
            dfs(node)
            res += 1
        
        return res