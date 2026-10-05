"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        if len(grid) == 0:
            return Node(False, False, None, None, None, None)
        total = 0
        m, n = len(grid), len(grid[0])#m by n
        for y in range(m):
            for x in range(n):
                total += grid[y][x]
        if total == 0:
            return Node(False, True, None, None, None, None)
        if total == (len(grid) * len(grid[0])):
            return  Node(True, True, None, None, None, None)
        else:
            curr_node = Node(True, False,None, None, None, None)
            curr_node.topLeft = self.construct([row[:(n//2)] for row in grid[:(m//2)]])
            curr_node.topRight = self.construct([row[(n//2):] for row in grid[:(m//2)]])
            curr_node.bottomLeft = self.construct([row[:(n//2)] for row in grid[(m//2):]])
            curr_node.bottomRight = self.construct([row[(n//2):] for row in grid[(m//2):]])
            return curr_node


