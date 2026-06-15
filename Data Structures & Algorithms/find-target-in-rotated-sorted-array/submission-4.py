class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            #if right half is not sorted, search right half
            if nums[mid] > nums[right]:
                left = mid + 1
            #right half is sorted. search left half
            else:
                right = mid
        pivot = left
        l, r = 0, len(nums) - 1
        if target <= nums[r]:
            l = pivot
        else:
            r = pivot - 1
        while l <= r:
            m = (l + r) //2
            if nums[m] == target:
                return m
            if nums[m] >= target:
                r = m - 1
            else:
                l = m + 1
        return -1

