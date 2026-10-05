class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        def neighbors(x, y):
            ns = []
            if x + 1 < n:
                ns.append([x+1, y])
            if x - 1 >= 0:
                ns.append([x-1, y])
            if y + 1 < m:
                ns.append([x, y+1])
            if y - 1 >= 0:
                ns.append([x, y-1])
            return ns
        def bfs(x, y):
            q = deque([[x, y]])
            area = 1
            while q:
                curr_x, curr_y = q.popleft()
                grid[curr_y][curr_x] = 0
                for n_x, n_y in neighbors(curr_x, curr_y):
                    if grid[n_y][n_x] == 1:
                        q.append([n_x, n_y])
                        grid[n_y][n_x] = 0
                        area += 1
            return area
        m, n = len(grid), len(grid[0])
        for y in range(m):
            for x in range(n):
                if grid[y][x] == 1:
                    curr_area = bfs(x, y)
                    area = max(area, curr_area)
        return area
                