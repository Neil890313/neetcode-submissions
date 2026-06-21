class ListNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
         self.cap = capacity
         self.cache = {}
         self.head = ListNode(0,0)
         self.tail = ListNode(0,0)
         self.head.next = self.tail
         self.tail.prev = self.head

    # helper function
    def _remove(self, node: ListNode):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_head(self, node: ListNode):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    # 實作1: 取得資訊
    def get(self, key: int) -> int:
        if key in self.cache:
            curr = self.cache[key]
            self._remove(curr)
            self._insert_head(curr)
            
            return curr.val
        else:
            return -1
    # 實作2: 插入/修改資料
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            old_node = self.cache[key]
            self._remove(old_node)
        
        new_node = ListNode(key, value)
        self.cache[key] = new_node
        self._insert_head(new_node)

        if len(self.cache) > self.cap:
           # Remove LRU node (the one before tail)
            lru_node = self.tail.prev
            self._remove(lru_node)
            
            # Remove from hashmap
            del self.cache[lru_node.key]
             
