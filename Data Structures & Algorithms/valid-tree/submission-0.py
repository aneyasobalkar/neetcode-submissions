class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) >= n:
            return False
        adjList = {i: [] for i in range(0, n)}
        for node1, node2 in edges:
            adjList[node1].append(node2)
            adjList[node2].append(node1)
        visited = set()
        cycle = set()
        def dfs(node, parent):
            if node in cycle:
                return False
            if node in visited:
                return True
            cycle.add(node)
            for neighbor in adjList[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            cycle.remove(node)
            visited.add(node)
            return True
        return dfs(0, -1) and len(visited) ==n