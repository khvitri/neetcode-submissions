class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != (n - 1):
            return False

        adj = {i: [] for i in range(n)}
        for edge in edges:
            a, b = edge
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()
        def dfs(node: int, parent: int) -> bool:
            # Cycle detected
            if node in visited:
                return False
            
            visited.add(node)
            for other in adj[node]:
                if other == parent:
                    continue
                
                if not dfs(other, node):
                    return False
            
            return True
        
        return dfs(0, -1) and len(visited) == n
