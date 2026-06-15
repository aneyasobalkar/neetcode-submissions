# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        first = head
        for i in range(n):
            first = first.next
        second = ListNode(-1, head)
        dummy = second
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next
        