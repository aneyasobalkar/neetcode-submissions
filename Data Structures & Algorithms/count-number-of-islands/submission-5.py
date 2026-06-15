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
        def dfs(m, n):
            stack = [(m,n)]
            while stack:
                y,x = stack.pop()
                #mark the island
                grid[y][x] = "0"
                #look though its neighbor
                adj = neighbors(y,x)
                for j, i in adj:
                    #if not marked
                    if grid[j][i] == "1":
                        stack.append((j, i))
        islands = 0
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == "1":
                    grid[m][n] = "0"
                    dfs(m, n)
                    islands += 1
                    
        return islands


    