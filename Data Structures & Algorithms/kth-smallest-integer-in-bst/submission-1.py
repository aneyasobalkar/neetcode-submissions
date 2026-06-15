# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [] #LIFO
        values = []
        curr = root
        while curr or stack:
            while curr:
                stack.insert(0,curr)
                curr = curr.left
            if not curr and stack:
                item = stack.pop(0)
                values.append(item.val)
                curr = item.right
        print(values)
        return values[k-1]
