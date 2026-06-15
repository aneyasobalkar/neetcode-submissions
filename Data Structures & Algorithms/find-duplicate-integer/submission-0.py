class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        left = 0 
        right = 1
        while right < len(nums):
            if nums[left] == nums[right]:
                return nums[left]
            else:
                left += 1
                right += 1