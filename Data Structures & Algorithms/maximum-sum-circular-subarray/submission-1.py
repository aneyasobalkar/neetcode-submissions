class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalMax = -30000
        n = len(nums)
        for index, num in enumerate(nums):
            gm = -30000
            lm = -30000
            for j in range(n):
                currNum = nums[((index + j)% n)]
                lm = max(lm + currNum, currNum)
                gm = max(lm, gm)
            globalMax = max(globalMax, gm)
        return globalMax