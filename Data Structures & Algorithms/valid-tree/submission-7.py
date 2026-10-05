class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #trees can only have up to n-1 edges
        if len(edges) >= n:
            return False
        adjlist = {i: [] for i in range(0,n)}
        for n1, n2 in edges:
            adjlist[n1].append(n2)
            adjlist[n2].append(n1)
        #use cycle detection
        visited = set()
        def dfs(curr_node, parent):
            if curr_node in visited:
                return False
            visited.add(curr_node)
            for neighbor in adjlist[curr_node]:
                if neighbor != parent:
                    if dfs(neighbor, curr_node) == False:
                        return False
            return True
        res = dfs(0, -1)
        return res if len(visited) == n else False

