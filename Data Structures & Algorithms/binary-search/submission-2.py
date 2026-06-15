class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        middle_index = len(nums)//2
        if nums[middle_index] == target:
            return middle_index
        elif nums[middle_index] > target:
            return self.search(nums[:middle_index], target)
        elif nums[middle_index] < target:
            right_search = self.search(nums[middle_index + 1: ], target)
            return middle_index + 1+right_search if right_search != -1 else -1