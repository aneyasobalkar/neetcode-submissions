class Solution:
    def jump(self, nums: List[int]) -> int:
        dp= [0]
        dp.extend([len(nums) for i in range(len(nums)-1)])
        for index, num in enumerate(nums):
            step = num
            for j in range(step+1):
                if index + j < len(nums):
                    dp[index + j] = min(dp[index + j], 1 + dp[index])
        return dp[-1]
        