class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        #solution ends when r = l, so r+l//2 = l
        while l < r:
            #not sorted
            k = (l + r) // 2
            #if we're in the unsorted region
            if nums[k] > nums[r]:
                #move the left pointer past k
                l = k + 1
            #if we're in the sorted region
            else:
                r = k
        return nums[r]
            