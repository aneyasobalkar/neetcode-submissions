class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        globalMax = nums[0]
        localMax = nums[0]
        localMin = nums[0]
        for num in nums[1:]:
            localMax, localMin = max(num, num*localMax, num * localMin),  min(num, num*localMax, num * localMin)
            globalMax = max(localMax, globalMax)
        return globalMax