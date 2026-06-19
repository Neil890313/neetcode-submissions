# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = None
        dummy = ListNode(0)
        curr = dummy
        while l1 and l2:
            add = l1.val + l2.val
            if carry:
                add = add + carry
            carry, b = divmod(add, 10)
            curr.next = ListNode(b)
            l1 = l1.next
            l2 = l2.next
            curr = curr.next
        while l1:
            add = l1.val
            if carry:
                add = add + carry
            carry, b = divmod(add, 10)
            curr.next = ListNode(b)
            l1 = l1.next
            curr = curr.next
        while l2:
            add = l2.val
            if carry:
                add = add + carry
            carry, b = divmod(add, 10)
            curr.next = ListNode(b)
            l2 = l2.next
            curr = curr.next
        if carry:
            curr.next = ListNode(carry)
        return dummy.next