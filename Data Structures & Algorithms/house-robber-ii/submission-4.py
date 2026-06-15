class Solution:
    def rob(self, nums: List[int]) -> int:
        def robHelper(nums):
            if len(nums) == 0:
                return 0
            if len(nums) == 1:
                return nums[0]
            dp = [nums[0], nums[1]]
            dp.extend([0 for i in range(len(nums)- 2)])
            max_val = max(dp)
            for index, num in enumerate(nums[2:], 2):
                new_sum = max(dp[:index-1]) + num
                max_val = max(max_val, new_sum)
                dp[index] = new_sum
            return max_val
        return max(nums[0], robHelper(nums[1:]), robHelper(nums[:-1]))