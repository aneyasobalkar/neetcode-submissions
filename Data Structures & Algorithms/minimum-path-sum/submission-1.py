class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[-1 for i in range(n)] for j in range(m)]
        def dfs(x,y):
            if x >= n or y >= m:
                return float("inf")
            if x == n -1 and y == m-1:
                dp[y][x] = grid[y][x]
                return grid[y][x]
            if dp[y][x] != -1:
                return dp[y][x]
            dp[y][x] = grid[y][x] + min(dfs(x+1, y),dfs(x,y+1))
            return dp[y][x]
        dfs(0,0)
        return dp[0][0]