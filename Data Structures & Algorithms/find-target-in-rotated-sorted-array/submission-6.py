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
        # --- DECIDE WHICH HALF TO LOOK IN ----
        if target <= nums[r]:
            #look in right half
            l = pivot
        else:
            #look in left half
            r = pivot
        while l <= r:
            m = (l + r) //2
            if nums[m] == target:
                return m
            if nums[m] > target:
                #look left
                r = m - 1
            else:
                #look right
                l = m + 1
        return -1

