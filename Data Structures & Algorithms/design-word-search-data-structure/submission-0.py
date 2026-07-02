class TrieNode:

    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
        
    def search(self, word: str) -> bool:
        stack = [(self.root, 0)]

        while stack:
            cur, i = stack.pop()
            
            if i >= len(word):
                return cur.endOfWord

            c = word[i]

            if c == ".":
                for child in cur.children.values():
                    stack.append((child, i + 1))
            elif c in cur.children:
                stack.append((cur.children[c], i + 1))
        
        return False

            



            
        
