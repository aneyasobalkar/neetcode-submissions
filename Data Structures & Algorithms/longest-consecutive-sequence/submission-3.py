class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        nums.sort()
        max_length = 0
        curr_len = 1
        j = 1
        while j < len(nums):
            diff = nums[j] - nums[j-1]
            if diff <= 1:
                curr_len += diff
            else:
                curr_len = 1
            j += 1
            max_length = max(max_length, curr_len)
        return max_length