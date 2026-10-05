# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def bfs(root):
            q = deque([[root, 0]])
            while q:
                node, level = q.popleft()
                if node:
                    if level >= len(res):
                        res.append([node.val])
                    else:
                        res[level].append(node.val)
                    if node.left:
                        q.append([node.left, level + 1]) 
                    if node.right:
                        q.append([node.right, level + 1]) 
        bfs(root)
        return res
                