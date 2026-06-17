class Node:

    def __init__(self, key: int , val: int):
        self.key, self.val = key, val
        self.nxt = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.nxt, self.right.prev = self.right, self.left      
    
    def _remove(self, node: Node):
        prev, nxt = node.prev, node.nxt
        prev.nxt, nxt.prev = nxt, prev 
        node.prev = node.nxt = None 
    
    def _insertR(self, node: Node):
        tail = self.right.prev 
        tail.nxt = self.right.prev = node
        node.prev, node.nxt = tail, self.right

    def get(self, key: int) -> int:
        if key in self.cache:
            self._remove(self.cache[key])            
            self._insertR(self.cache[key])
            return self.cache[key].val 
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self._insertR(self.cache[key])

        if len(self.cache) > self.cap:
            head = self.left.nxt
            self._remove(head)  
            del self.cache[head.key]
