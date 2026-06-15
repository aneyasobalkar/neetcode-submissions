class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def neighbors(x, y):
            arr = []
            if x+1 < len(heights[0]):
                arr.append((x+1, y))
            if x-1>=0:
                arr.append((x-1, y))
            if y+1 < len(heights):
                arr.append((x, y+1))
            if y-1 >= 0:
                arr.append((x, y-1))
            return arr
        def dfs(x, y, prevHeight, visited):
            if heights[y][x] < prevHeight or (x,y) in visited:
                return
            visited.add((x, y))
            for n_x, n_y in neighbors(x, y):
                dfs(n_x, n_y,heights[y][x], visited)
        pac = set()
        atl = set()
        ROWS, COLS = len(heights), len(heights[0])
        for r in range(0,ROWS):
            dfs(0, r, heights[r][0], pac)
            dfs(COLS-1, r,  heights[r][COLS-1], atl)
        for c in range(0,COLS):
            dfs(c, 0, heights[0][c], pac)
            dfs(c, ROWS - 1, heights[ROWS-1][c], atl)

        res = []
        for p_x, p_y in pac:
            if (p_x, p_y) in atl:
                res.append([p_y, p_x])
        return res

