class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        arr = [-1]
        arr.extend([0 for i in range(1, len(nums))]) #[-1, 0,0 0, 0]
        for num in nums:
            if arr[num] == 1:
                return num
            else:
                arr[num] += 1


