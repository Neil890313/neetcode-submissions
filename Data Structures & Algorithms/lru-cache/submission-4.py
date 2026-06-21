class ListNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = ListNode(0,0)
        self.tail = ListNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    # helper function
    # insert
    def _insert(self, node):
        tmp = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = tmp
        tmp.prev = node
    # delete
    def _delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._delete(node)
            self._insert(node)

            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            old_node = self.cache[key]
            self._delete(old_node)
        
        new = ListNode(key, value)
        self.cache[key] = new
        self._insert(new)

        if len(self.cache) > self.capacity:
            curr = self.tail.prev
            self._delete(curr)
            del self.cache[curr.key]

















