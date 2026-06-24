# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        second_head = slow.next
        slow.next = None
        first_head = head

        prev = None
        curr = second_head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        second_head = prev
        
        while second_head:
            next1 = first_head.next
            next2 = second_head.next
            first_head.next = second_head
            second_head.next = next1
            first_head = next1
            second_head = next2





        