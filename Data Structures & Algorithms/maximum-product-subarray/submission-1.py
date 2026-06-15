class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        globalMax = nums[0]
        localMax = nums[0]
        localMin = nums[0]
        for index, num in enumerate(nums[1:], 1):
            localMax, localMin = max(nums[index], nums[index]*localMax, nums[index] * localMin),  min(nums[index], nums[index]*localMax, nums[index] * localMin)
            globalMax = max(localMax, globalMax)
        return globalMax