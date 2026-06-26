class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        dp = [False for i in range(len(nums))]
        def dfs(nums, total, ind):
            if ind < len(nums) and dp[ind]:
                return dp[ind]
            if total < 0:
                return False
            if len(nums) == 0:
                return True if total == 0 else False
            w = dfs(nums[1:], total - nums[0], ind + 1)
            wo = dfs(nums[1:], total, ind + 1)
            dp[ind] = w or wo
            return dp[ind]
        dfs(nums, sum(nums) // 2, 0)
        return dp[0]