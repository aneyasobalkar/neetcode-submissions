class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            #not sorted
            k = (l + r) // 2
            #if we're in the unsorted region
            if nums[k] > nums[r]:
                #move the left pointer past k
                l = k + 1
            #if we're in the sorted region
            #elif nums[l] > nums[k]:
                #move the left pointer
                #l = k
            else:
                r = k
        return nums[l]
            