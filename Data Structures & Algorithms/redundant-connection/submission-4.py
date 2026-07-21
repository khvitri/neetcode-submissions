class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = {i: [] for i in range(1, n + 1)}

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited, cycleNode = set(), set()
        startCycle = -1
        done = False

        def dfs(node: int, parent: int):
            nonlocal done, startCycle

            if done:
                return

            if node in visited:
                startCycle = node
                cycleNode.add(node)
                return

            visited.add(node)
            for neigh in adj[node]:
                if neigh == parent:
                    continue
                dfs(neigh, node)                 

                if startCycle == node: 
                    startCycle = -1
                    done = True
                    break

                if startCycle != -1:
                    cycleNode.add(node)
                    break
                
        
        dfs(1, -1)

        for i in range(len(edges) - 1, -1, -1):
            a, b = edges[i]
            if a in cycleNode and b in cycleNode:
                return edges[i]
        
        return [-1 , -1]

                    

            

