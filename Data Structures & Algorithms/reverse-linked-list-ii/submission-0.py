# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        linkedmap = {}
        curr = head
        for i in range(1, right + 1):
            linkedmap[i] = curr
            curr = curr.next
        while left <= right:
            linkedmap[left].val, linkedmap[right].val = linkedmap[right].val, linkedmap[left].val
            left+=1
            right -=1
        return head