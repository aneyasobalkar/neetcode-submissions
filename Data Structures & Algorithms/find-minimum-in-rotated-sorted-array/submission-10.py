class Solution:
    def findMin(self, nums: List[int]) -> int:  
        left = 0
        right = len(nums) - 1
        curr = nums[0]
        while left <= right:
            #if range is sorted
            if nums[left] < nums[right]:
                curr = min(curr, nums[left])
                return curr
            mid = (right + left) // 2
            curr = min(curr, nums[mid])
            #search left range or right range
            #if left side sorted, min is in the right range then
            if nums[left] <= nums[mid]:
                left = mid + 1
            #if left side is not sorted, min is in the left
            else:
                right = mid - 1
        return curr
        
        # check prev val and the one ahead
        # if in prev, mid, ahead in order -> look form nums[ahead: ]
        #else: look from nums[: ahead]
