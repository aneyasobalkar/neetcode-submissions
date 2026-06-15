class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def neighbors(x, y):
            arr = []
            if x + 1 < len(grid[0]):
                arr.append((x+1, y))
            if x - 1 >= 0:
                arr.append((x-1, y))
            if y + 1 < len(grid):
                arr.append((x, y+1))
            if y - 1 >= 0:
                arr.append((x, y-1))
            return arr
        def bfs(x, y):
            queue = [(x,y)]
            while queue:
                itemX, itemY = queue.pop(0)
                for n_x, n_y in neighbors(itemX, itemY):
                    if grid[n_y][n_x] != -1 and 1+grid[itemY][itemX] < grid[n_y][n_x]:
                        queue.append((n_x, n_y))
                        grid[n_y][n_x] = 1+grid[itemY][itemX]
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 0:
                    bfs(x, y)
