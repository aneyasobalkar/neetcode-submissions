class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        print(m, n)
        dp = [[0 for j in range(n)] for i in range(m)]
        def dfs(i, j):
            #if we are out of bounds
            if i >= m or j >= n or obstacleGrid[i][j] == 1:
                return 0
            #if we reach the bottom of the grid
            if i == (m-1) and j == (n-1):
                return 1
            if dp[i][j]:
                return dp[i][j]
            dp[i][j] = dfs(i+1,j) + dfs(i, j+1)
            return dp[i][j]
        return dfs(0,0)
        #return dp[0][0]