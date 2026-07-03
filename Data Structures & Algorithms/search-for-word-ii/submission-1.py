class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word: str) -> None:
        cur = self

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = set()
        root = self.buildTrie(words)

        visited = set()
        def searchWords(r: int, c: int, node: TrieNode, w: str) -> None:
            if node.isWord:
                res.add(w)

            if (r < 0 or 
              c < 0 or 
              r >= len(board) or 
              c >= len(board[0]) or 
              (r, c) in visited):
                return
            
            char = board[r][c]
            if char in node.children:
                visited.add((r, c))
                child = node.children[char]
                searchWords(r - 1, c, child, w + char)
                searchWords(r, c + 1, child, w + char)
                searchWords(r + 1, c, child, w + char)
                searchWords(r, c - 1, child, w + char)
                visited.remove((r, c))
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                searchWords(r, c, root, "")
        
        return list(res)

    def buildTrie(self, words: List[str]) -> TrieNode:
        root = TrieNode()

        for w in words:
            root.addWord(w)

        return root  
        