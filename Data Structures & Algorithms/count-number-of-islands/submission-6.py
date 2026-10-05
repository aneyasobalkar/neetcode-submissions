from collections import deque
class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        def neighbors(row, col):
            ns = []
            if row + 1 < m:
                ns.append([row+1, col])
            if col + 1 < n:
                ns.append([row, col+1])
            if col - 1>= 0:
                ns.append([row, col-1])
            if row -1>= 0:
                ns.append([row-1, col])
            return ns
            #compute the neighbors 
        def bfs(row, col): # 0 is water and 1 is land
            q = deque([[row, col]])
            #while deque is not empty
            while q:
                #print(q.pop())
                y, x = q.pop()
                grid[y][x] = "0"
                for n_y, n_x in neighbors(y, x):
                    if grid[n_y][n_x] == "1":
                        q.append([n_y, n_x])

       
        islands = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
        return islands
        


    