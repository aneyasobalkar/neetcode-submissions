class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        
        #[2,3,4,4,5,10,20]
        #[0,1,1,2,3,4,5,6]
        nums.sort()
        max_length = 0
        curr_len = 1
        j = 1
        while j < len(nums):
            if nums[j] - nums[j-1] <= 1:
                curr_len += (nums[j] - nums[j-1])
            else:
                curr_len = 1
            j += 1
            max_length = max(max_length, curr_len)
        return max_length