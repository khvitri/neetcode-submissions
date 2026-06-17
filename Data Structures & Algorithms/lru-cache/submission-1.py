class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self._lru = dict() # Doubly linked-list 
        self._head = None
        self._tail = None

    def get(self, key: int) -> int:
        value = self.cache.get(key, -1)                
        if value >= 0:
            self._moveToLast(key) 
        print(f"GET: {key} - {self._lru}")
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self._moveToLast(key)
            return
        
        if len(self.cache) >= self.capacity:
            del self.cache[self._head]
            self._removeHead()
            
        self.cache[key] = value
        self._addTail(key)
        print(f"PUT: ({key}, {value}) - {self._lru}")

    def _addTail(self, key) -> None: 
        if not self._tail and not self._head:
            self._lru[key] = [None, None]
            self._tail = key
            self._head = key
            return

        self._lru[self._tail][1] = key
        self._lru[key] = [self._tail, None]
        self._tail = key

    def _removeHead(self) -> None: 
        oldHead = self._head
        if self._tail == self._head:
            self._head = None
            self._tail = None
        else:
            self._head = self._lru[self._head][1]
            self._lru[self._head][0] = None
        
        del self._lru[oldHead]
    
    def _moveToLast(self, key: int) -> None:
        if key == self._tail: return

        keyPrev = self._lru[key][0]                       # Key's previous
        keyNext = self._lru[key][1]
        if key == self._head:
            self._head = self._lru[key][1]                # Head becomes curr. head's next
            self._lru[self._head][0] = None
        else:
            self._lru[keyPrev][1] = keyNext     # Key previous's next becomes key's next
            self._lru[keyNext][0] = keyPrev

        # Key's next and prev. is modified
        self._lru[key][0] = self._tail # Key's prev. is the curr. tail
        self._lru[key][1] = None       # Key's next becomes None

        # Curr. tail next becomes the key placed at the last
        self._lru[self._tail][1] = key

        # Tail becomes the key 
        self._tail = key 

        
