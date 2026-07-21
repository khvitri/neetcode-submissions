class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not endWord in wordList: return 0

        def isDiffOneChar(a: str, b: str) -> bool:
            diff = False
            for i in range(len(a)):
                if a[i] != b[i]:
                    if diff:
                        return False
                    diff = True
            return True

        adj = {word: set() for word in wordList}
        for word in wordList:
            for curr in wordList:
                if word == curr:
                    continue
                if isDiffOneChar(word, curr):
                    adj[word].add(curr)
                    adj[curr].add(word)
        
        q = deque()
        visited = set()

        def bfs() -> int:
            level = 1
            while q:
                for i in range(len(q)):
                    word = q.popleft()

                    if word in visited:
                        continue
                    
                    if word == endWord:
                        return level + 1

                    visited.add(word)
                    for neigh in adj[word]:
                        q.append(neigh)
                
                level += 1
            
            return 0

        for word in wordList:
            if isDiffOneChar(word, beginWord):
                q.append(word)
        
        return bfs()
        

                

            