# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0)
        curr = dummy
        while l1 or l2 or carry:
            l1_num = 0 if not l1 else l1.val
            l2_num = 0 if not l2 else l2.val
            total = l1_num + l2_num + carry
            carry, remain = divmod(total, 10)
            new = ListNode(remain)
            curr.next = new
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next
