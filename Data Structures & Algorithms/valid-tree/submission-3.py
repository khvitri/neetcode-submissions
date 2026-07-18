class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != (n - 1):
            return False
        
        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs(root: int) -> bool:
            stack = [[root, -1]]
            
            visited = set()
            while stack:
                node, parent = stack.pop()

                # Cycle detected
                if node in visited:
                    return False
                
                visited.add(node)
                for neigh in adj[node]:
                    if neigh != parent:
                        stack.append([neigh, node])

            return len(visited) == n
        
        return dfs(0)