"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        oldToNew = {}
        oldToNew[node] = Node(node.val)
        stack = [node]
        while stack:
            item = stack.pop()
           #if item:
            for neighbor in item.neighbors:
                if neighbor not in oldToNew:
                    stack.append(neighbor)
                    oldToNew[neighbor] = Node(neighbor.val)
        for old, new in oldToNew.items():
            new.neighbors = [oldToNew[old] for old in old.neighbors]
        return oldToNew[node]


