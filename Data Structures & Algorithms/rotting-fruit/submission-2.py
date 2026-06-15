class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.minutes = 0
        def neighbors(x, y):
            arr = []
            if x+1 < len(grid[0]):
                arr.append((x+1, y))
            if x-1>= 0:
                arr.append((x-1, y))
            if y-1>= 0:
                arr.append((x, y-1))
            if y+1 < len(grid):
                arr.append((x, y+1))
            return arr
        def bfs(queue):
            #queue = [(x,y,0)]
            while queue:
                itemx, itemy, lvl = queue.pop(0)
                for n_x, n_y in neighbors(itemx, itemy):
                    if grid[n_y][n_x] == 1:
                        grid[n_y][n_x] = 2
                        queue.append((n_x, n_y, lvl+1))
                self.minutes = max(self.minutes, lvl)
        q = []
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 2:
                    q.append((x,y, 0))
        bfs(q)
        for y in range(len(grid)):
            if 1 in grid[y]:
                return -1
        return self.minutes