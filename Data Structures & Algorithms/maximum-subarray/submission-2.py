class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        globalMax = nums[0]
        localMax = 0
        for n in nums:
            if localMax < 0:
                localMax = 0
            localMax += n
            globalMax= max(globalMax, localMax)
        return globalMax