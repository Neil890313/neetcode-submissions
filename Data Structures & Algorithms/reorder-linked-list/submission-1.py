# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Step1:將目前的 list 切成兩半
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        second_head = slow.next
        slow.next = None

        # Step:翻轉後半段
        prev = None
        curr = second_head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # Step3:縫合
        first_head, second_head = head, prev
        while second_head:
            tmp1 = first_head.next
            tmp2 = second_head.next

            first_head.next = second_head
            second_head.next = tmp1

            first_head = tmp1
            second_head = tmp2