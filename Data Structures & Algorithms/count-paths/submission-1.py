class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for j in range(n)] for i in range(m)]

        def dfs(j, i):
            if j >= m or i >= n:
                return 0
            if dp[j][i]:
                return dp[j][i]
            if j == m-1 and i == n-1:
                return 1
            if dp[j][i]:
                return dp[j][i]
            dp[j][i] = dfs(j+1, i) + dfs(j, i+1)
            return dp[j][i] 
        return dfs(0, 0)
        