class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums))]
        for i in range(len(nums)):
            if i - 2 >= 0:
                dp[i] = nums[i] + max(dp[0:i-1])
            else:
                dp[i] = nums[i]
        return max(dp)