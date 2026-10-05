class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = list(nums)
        for i in range(n-1, -1, -1):
            if i + 2 < len(nums):
                dp[i] += max(dp[i+2: ])
        return max(dp)