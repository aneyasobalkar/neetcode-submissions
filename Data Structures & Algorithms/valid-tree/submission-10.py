class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #trees can only have up to n-1 edges
        if len(edges) != n-1:
            return False
        adjlist = {i: [] for i in range(0,n)}
        for n1, n2 in edges:
            adjlist[n1].append(n2)
            adjlist[n2].append(n1)
        #use cycle detection
        visited = set()
        def bfs(curr_node, parent):
            #if a node we have visited is a neighbor -> cycle
            q = deque([[curr_node, parent]])
            while q:
                c, p = q.popleft()
                visited.add(c)
                for neighbor in adjlist[c]:
                    if neighbor == p:
                        continue
                    if neighbor in visited:
                        return False
                    else:
                        q.append([neighbor, c])
            return True
        res = bfs(0, -1)
        return res if len(visited) == n else False #have we visited every node? fully connected?

