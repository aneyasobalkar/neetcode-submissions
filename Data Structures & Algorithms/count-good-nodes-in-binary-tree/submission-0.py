# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root, maxInPath):
            if not root:
                return 0
            if root.val < maxInPath:
                return helper(root.left, maxInPath) + helper(root.right, maxInPath)
            else:
                return 1 + helper(root.left, root.val) + helper(root.right, root.val)
        return helper(root, -101)