class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def neighbors(x, y):
            arr = []
            if x + 1 < len(grid[0]):
                arr.append((x+1, y))
            if x - 1 >= 0:
                arr.append((x-1, y))
            if y - 1 >= 0:
                arr.append((x, y-1))
            if y + 1 < len(grid):
                arr.append((x, y+1))
            return arr
        def dfsArea(x, y):
            stack = [(x,y)]
            area = 0
            while stack:
                xpos, ypos = stack.pop()
                area += 1
                for n_x, n_y in neighbors(xpos, ypos):
                    if grid[n_y][n_x] == 1:
                        stack.append((n_x, n_y))
                        grid[n_y][n_x] = 0
            return area

        maxArea = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    grid[y][x] = 0
                    area = dfsArea(x,y)
                    maxArea = max(area, maxArea)
        return maxArea