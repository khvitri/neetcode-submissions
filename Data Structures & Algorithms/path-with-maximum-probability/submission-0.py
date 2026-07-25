class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = {i: [] for i in range(n)}
        for i in range(len(edges)):
            a, b = edges[i]
            p = succProb[i]
            adj[a].append((b, p))
            adj[b].append((a, p))
        
        maxHeap = [(-1, start_node)]
        visit = set()
        while maxHeap:
            p, n = heapq.heappop(maxHeap)

            if n == end_node:
                return -p

            if n in visit:
                continue

            visit.add(n)
            for neigh, neighProb in adj[n]:
                if neigh in visit:
                    continue
                heapq.heappush(maxHeap, (p * neighProb, neigh))
        
        return 0
            


