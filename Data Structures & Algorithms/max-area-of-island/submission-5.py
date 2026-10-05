class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        maxArea = 0
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
        def bfs(row, col): # 0 is water and 1 is land
            area = 0
            q = deque([[row, col]])
            grid[row][col] = 0
            while q:
                y, x = q.pop()
                area += 1
                for n_y, n_x in neighbors(y, x):
                    if grid[n_y][n_x] == 1:
                        q.append([n_y, n_x])
                        grid[n_y][n_x] = 0
            return area
        islands = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    curr_area = bfs(r, c)
                    maxArea = max(curr_area, maxArea)
        return maxArea
                