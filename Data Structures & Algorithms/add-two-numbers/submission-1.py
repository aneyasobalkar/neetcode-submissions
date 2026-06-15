# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = l1
        num_first = 0
        multiplier = 1
        while first:
            num_first += (multiplier * first.val)
            first = first.next
            multiplier *= 10
        second = l2
        num_second = 0
        multiplier = 1
        while second:
            num_second += (multiplier * second.val)
            second = second.next
            multiplier *= 10
        total = str(num_first + num_second)[::-1]
        total_list = None
        for i in range(len(total)-1, -1, -1):
            total_list = ListNode(int(total[i]), total_list)
        return total_list

        