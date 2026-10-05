class Solution:
    def numSquares(self, n: int) -> int:
        choices = []
        i = 1 
        while i*i <= n:
            choices.append(i*i)
            i+=1
        choices = choices[::-1]
        dp = [float("inf") for i in range(n+1)]
        dp[0]=0
        for target in range(n+1):
            for choice in choices:
                if target - choice >= 0:
                    dp[target] = min(dp[target], 1+ dp[target-choice])
        return dp[n]
