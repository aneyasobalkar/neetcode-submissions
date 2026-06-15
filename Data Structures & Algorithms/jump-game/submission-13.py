class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        goal = len(nums) - 1
        start = goal - 1
        for index in range(start, -1, -1):
            if nums[index] + index >= goal:
                goal = index
        return goal == 0