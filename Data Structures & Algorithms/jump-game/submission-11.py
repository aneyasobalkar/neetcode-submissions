class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        goal = len(nums) - 1
        start = goal - 1
        while start > 0:
            step = nums[start]
            #even with max jump length, we cant reach goal lets start somewhere else
            if step + start < goal:
                start -= 1
            else:
                #we can jump to the goal. 
                #now we want to see if we can jump to our current pos
                nums[start] -=1
                goal = start
        #one last check
        return nums[start] + start >= goal