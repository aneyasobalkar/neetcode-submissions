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
        visited = {node:  Node(node.val)}
        stack = [node]
        while stack:
            item = stack.pop()
            for neighbor in item.neighbors:
                #if neighbor has not been marked
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited[neighbor] = Node(neighbor.val)
        for old, new in visited.items():
            new.neighbors = [visited[old] for old in old.neighbors]
        return visited[node]


