class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return min(nums)
        left = 0
        right = len(nums) - 1
        curr = nums[0]
        while left <= right:
            if nums[left] < nums[right]:
                curr = min(curr, nums[left])
                return curr
            mid = (right + left) // 2
            curr = min(curr, nums[mid])
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return curr
        
        # check prev val and the one ahead
        # if in prev, mid, ahead in order -> look form nums[ahead: ]
        #else: look from nums[: ahead]
