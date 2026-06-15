class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def neighbors(m, n):
            ret = []
            if m-1 >= 0:
                ret.append((m-1,n))
            if m+1 < len(grid):
                ret.append((m+1,n))
            if n -1 >= 0:
                ret.append((m,n-1))
            if n + 1 < len(grid[0]):
                ret.append((m,n+1))
            return ret
        
        islands = 0
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == "1":
                    islands += 1
                    stack = [(m,n)]
                    grid[m][n] = "0"
                    while stack:
                        y,x = stack.pop()
                        grid[y][x] = "0"
                        adj = neighbors(y,x)
                        for j, i in adj:
                            if grid[j][i] == "1":
                                stack.append((j, i))
        return islands


    