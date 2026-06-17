class Node:

    def __init__(self, key=0, val=0, prev=None, nxt=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt
    
    def assignNext(self, other: Node) -> None:
        self.nxt = other
        other.prev = self
    
    def assignPrev(self, other: Node) -> None:
        self.prev = other
        other.nxt = self

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.head, self.tail = Node(), Node()
        self.head.assignNext(self.tail)

    def moveToTail(self, node: Node) -> None:
        nodeNxt = node.nxt
        nodePrev = node.prev

        nodeNxt.assignPrev(nodePrev)

        nodeLast = self.tail.prev
        nodeLast.assignNext(node)
        node.assignNext(self.tail)

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.moveToTail(node)
            return node.val
        
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.moveToTail(node)
            return

        newNode = self.cache[key] = Node(key, value)
        nodeLast = self.tail.prev
        nodeLast.assignNext(newNode)
        newNode.assignNext(self.tail)

        if len(self.cache) > self.capacity:
            lruNode = self.head.nxt
            self.head.assignNext(lruNode.nxt)
            del self.cache[lruNode.key]
        
        return


        
