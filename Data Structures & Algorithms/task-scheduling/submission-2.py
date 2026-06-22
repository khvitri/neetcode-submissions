class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = defaultdict(int)
        for task in tasks:
            count[task] += 1
        
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        q = deque()
        cycle = 0

        while maxHeap or q: 
            if q and q[0][1] == cycle:
                qTask = q.popleft()[0]
                heapq.heappush(maxHeap, qTask)

            if maxHeap:
                maxTask = heapq.heappop(maxHeap)
                remainingTask = maxTask + 1 # Process the max task
    
                if remainingTask < 0:
                    executeCycle = cycle + n + 1
                    q.append((remainingTask, executeCycle))
             
            cycle += 1
        
        return cycle
            
                
