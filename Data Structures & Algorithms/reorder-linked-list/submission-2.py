# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # step1: 找到中間點
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second_head = slow.next
        slow.next = None

        # step2: 反轉後半
        prev = None
        curr = second_head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        first_head = head
        second_head = prev
        
        # step3: zip
        while second_head:
            nxt1 = first_head.next
            nxt2 = second_head.next
            first_head.next = second_head
            second_head.next = nxt1
            first_head = nxt1
            second_head = nxt2




        