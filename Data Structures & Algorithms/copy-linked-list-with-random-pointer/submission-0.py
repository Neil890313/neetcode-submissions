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

        dummy = Node(0)
        new = dummy
        old = head

        while old: 
            tmp = old2new_dict[old]
            tmp.random = old2new_dict[old.random]
            tmp.next = old2new_dict[old.next]
            new.next = tmp
            new = new.next
            old = old.next
        
        return dummy.next