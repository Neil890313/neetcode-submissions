"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old2new_dict = {None: None}
        curr = head
        while curr:
            old2new_dict[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            node = old2new_dict[curr]
            node.random = old2new_dict[curr.random]
            node.next = old2new_dict[curr.next]
            curr = curr.next
        return old2new_dict[head]