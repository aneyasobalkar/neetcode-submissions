# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        mid_point = head
        fast_pointer = head.next
        while fast_pointer and fast_pointer.next:
            mid_point = mid_point.next
            fast_pointer = fast_pointer.next.next
        #slow pointer is midpoint
        right_half = mid_point.next
        mid_point.next = None
        stack = []
        while right_half:
            stack.append(right_half)
            right_half = right_half.next
        pointer = head
        while stack:
            val = stack.pop()
            pointer.next = ListNode(val.val, pointer.next)
            pointer = pointer.next.next





    