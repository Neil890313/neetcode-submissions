class ListNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = ListNode(0,0)
        self.tail = ListNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    # helper function
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _insert_head(self, node):
        nxt = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = nxt
        nxt.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert_head(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
        new = ListNode(key, value)
        self.cache[key] = new
        self._insert_head(new)

        if len(self.cache) > self.capacity:
            LRU = self.tail.prev
            self._remove(LRU)
            del self.cache[LRU.key]

