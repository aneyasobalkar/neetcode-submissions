"""
# Definition for a Node.
from os import curdir
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        old_to_new = {}
        #create hashmap of old to new nodes
        def dfs(curr_node):
            if curr_node in old_to_new:
                return
            old_to_new[curr_node] = Node(curr_node.val)
            for neighbor in curr_node.neighbors:
                #if neighbor not in visited:
                    #visited.add(neighbor)
                dfs(neighbor)
                old_to_new[curr_node].neighbors.append(old_to_new[neighbor])
                #old_to_new[neighbor].neighbors.append(old_to_new[curr_node])
        dfs(node)
        return old_to_new[node]


