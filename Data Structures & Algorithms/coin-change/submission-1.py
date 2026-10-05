class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {0:0}
        def dfs(value):
            if value < 0:
                return float("inf")
            if value == 0:
                return 0
            if value in dp:
                return dp[value]
            res = float("inf")
            for coin in coins:
                res = min(dfs(value-coin)+1, res)
            dp[value] = res
            return res
        total = dfs(amount)
        return total if total != float('inf') else -1