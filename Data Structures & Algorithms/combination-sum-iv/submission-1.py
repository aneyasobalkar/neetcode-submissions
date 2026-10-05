class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {}
        dp[0] = 1
        for goal in range(0, target+1):
            if goal not in dp:
                dp[goal] = 0
            for num in nums:
                dp[goal] += dp.get(goal-num, 0)
        return dp[target]

        