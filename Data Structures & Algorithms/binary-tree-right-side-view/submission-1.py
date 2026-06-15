# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def bfs(root):
            queue = [(root, 0)]
            trav = []
            while queue:
                node, lvl = queue.pop(0)
                if node:
                    if node.left:
                        queue.append((node.left, lvl + 1))
                    if node.right:
                        queue.append((node.right, lvl + 1))
                    if lvl >= len(trav):
                        trav.append([(node.val, lvl)])
                    else:
                        trav[lvl].append((node.val, lvl))
            return trav
        trav = bfs(root)
        return [trav_list[-1][0] for trav_list in trav]